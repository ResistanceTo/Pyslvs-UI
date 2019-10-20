# -*- coding: utf-8 -*-

"""The source code refer from "spatial_efd" module."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import Tuple, Sequence
from math import pi, sin, cos, atan2, degrees, radians
from numpy import (
    sqrt,
    abs,
    cos as np_cos,
    sin as np_sin,
    dot,
    sum as np_sum,
    array,
    ndarray,
    linspace,
    zeros,
    ones,
    diff,
    concatenate,
    cumsum,
)


def normalize_efd(
    coeffs: ndarray,
    size_invariant: bool = True
) -> Tuple[ndarray, float]:
    """
    Normalize the Elliptical Fourier Descriptor coefficients for a polygon.

    Implements Kuhl and Giardina method of normalizing the coefficients
    An, Bn, Cn, Dn. Performs 3 separate normalizations. First, it makes the
    data location invariant by re-scaling the data to a common origin.
    Secondly, the data is rotated with respect to the major axis. Thirdly,
    the coefficients are normalized with regard to the absolute value of A_1.
    This code is adapted from the pyefd module. See the original paper for
    more detail:

    Kuhl, FP and Giardina, CR (1982). Elliptic Fourier features of a closed
    contour. Computer graphics and image procesnp_sing, 18(3), 236-258.

    Args:
        coeffs: A numpy array of shape (n, 4) representing the
            four coefficients for each harmonic computed.
        size_invariant: Set to True (the default) to perform the third
            normalization and false to return the data withot this procesnp_sing
            step. Set this to False when plotting a comparison between the
            input data and the Fourier ellipse.
    Returns:
        A tuple consisting of a numpy.ndarray of shape (harmonics, 4)
        representing the four coefficients for each harmonic computed and
        the rotation in degrees applied to the normalized contour.
    """
    # Make the coefficients have a zero phase shift from
    # the first major axis. Theta_1 is that shift angle.
    theta_1 = atan2(
        2 * (coeffs[0, 0] * coeffs[0, 1] + coeffs[0, 2] * coeffs[0, 3]),
        coeffs[0, 0] ** 2 - coeffs[0, 1] ** 2 + coeffs[0, 2] ** 2 - coeffs[0, 3] ** 2
    ) * 0.5
    # Rotate all coefficients by theta_1.
    for n in range(1, coeffs.shape[0] + 1):
        coeffs[n - 1, :] = dot(
            array([
                [coeffs[n - 1, 0], coeffs[n - 1, 1]],
                [coeffs[n - 1, 2], coeffs[n - 1, 3]],
            ]),
            array([
                [np_cos(n * theta_1), -np_sin(n * theta_1)],
                [np_sin(n * theta_1), np_cos(n * theta_1)],
            ])
        ).flatten()
    # Make the coefficients rotation invariant by rotating so that
    # the semi-major axis is parallel to the x-axis.
    psi_1 = atan2(coeffs[0, 2], coeffs[0, 0])
    psi_r = array([
        [np_cos(psi_1), np_sin(psi_1)],
        [-np_sin(psi_1), np_cos(psi_1)],
    ])
    # Rotate all coefficients by -psi_1.
    for n in range(1, coeffs.shape[0] + 1):
        rot = array([
            [coeffs[n - 1, 0], coeffs[n - 1, 1]],
            [coeffs[n - 1, 2], coeffs[n - 1, 3]],
        ])
        coeffs[n - 1, :] = psi_r.dot(rot).flatten()
    if size_invariant:
        # Obtain size-invariance by normalizing.
        coeffs /= abs(coeffs[0, 0])
    return coeffs, degrees(psi_1)


def calculate_dc_coefficients(
    zx: Sequence[float],
    zy: Sequence[float]
) -> Tuple[float, float]:
    """
    Compute the dc coefficients, used as the locus when calling
    inverse_transform().

    This code is adapted from the pyefd module. See the original paper for
    more detail:

    Kuhl, FP and Giardina, CR (1982). Elliptic Fourier features of a closed
    contour. Computer graphics and image procesnp_sing, 18(3), 236-258.

    Args:
        zx: A list (or numpy array) of x coordinate values.
        zy: A list (or numpy array) of y coordinate values.
    Returns:
        A tuple containing the c and d coefficients.
    """
    contour = array([(x, y) for x, y in zip(zx, zy)])
    dxy = diff(contour, axis=0)
    dt = sqrt((dxy ** 2).sum(axis=1))
    t = concatenate(([0], cumsum(dt)))
    zt = t[-1]
    diffs = diff(t ** 2)
    xi = cumsum(dxy[:, 0]) - dxy[:, 0] / dt * t[1:]
    a0 = 1 / zt * np_sum(dxy[:, 0] / (2 * dt) * diffs + xi * dt)
    delta = cumsum(dxy[:, 1]) - dxy[:, 1] / dt * t[1:]
    c0 = 1 / zt * np_sum(dxy[:, 1] / (2 * dt) * diffs + delta * dt)
    # A0 and CO relate to the first point of the contour array as origin.
    # Adding those values to the coeffs to make them relate to true origin
    return contour[0, 0] + a0, contour[0, 1] + c0


def inverse_transform(
    coeffs: ndarray,
    locus: Tuple[float, float] = (0., 0.),
    n: int = 300,
    harmonic: int = 10
) -> Tuple[ndarray, ndarray]:
    """
    Perform an inverse fourier transform to convert the coefficients back into
    spatial coordinates.

    Implements Kuhl and Giardina method of computing the performing the
    transform for a specified number of harmonics. This code is adapted
    from the pyefd module. See the original paper for more detail:

    Kuhl, FP and Giardina, CR (1982). Elliptic Fourier features of a closed
    contour. Computer graphics and image procesnp_sing, 18(3), 236-258.

    Args:
        coeffs: A numpy array of shape (n, 4) representing the
            four coefficients for each harmonic computed.
        locus: The x,y coordinates of the centroid of the contour being
            generated. Use calculate_dc_coefficients() to generate the correct
            locus for a shape.
        n: The number of coordinate pairs to compute. A larger value will
            result in a more complex shape at the expense of increased
            computational time. Defaults to 300.
        harmonic: The number of harmonics to be used to generate
            coordinates, defaults to 10. Must be <= coeffs.shape[0]. Supply a
            smaller value to produce coordinates for a more generalized shape.
    Returns:
        A numpy array of shape (harmonics, 4) representing the
        four coefficients for each harmonic computed.
    """
    t = linspace(0, 1, n)
    xt = ones(n) * locus[0]
    yt = ones(n) * locus[1]
    for n in range(harmonic):
        xt += (
            coeffs[n, 2] * np_cos(2. * (n + 1) * pi * t) +
            coeffs[n, 3] * np_sin(2. * (n + 1) * pi * t)
        )
        yt += (
            coeffs[n, 0] * np_cos(2. * (n + 1) * pi * t) +
            coeffs[n, 1] * np_sin(2. * (n + 1) * pi * t)
        )
    return xt, yt


def nyquist(zx: Sequence[float]) -> int:
    """
    Returns the maximum number of harmonics that can be computed for a given
    contour, the Nyquist Frequency.

    See this paper for details:
    C. np_costa et al. / Postharvest Biology and Technology 54 (2009) 38-47

    Args:
        zx (list): A list (or numpy array) of x coordinate values.
    Returns:
        int: The nyquist frequency, expressed as a number of harmonics.
    """
    return len(zx) // 2


def calculate_efd(
    zx: Sequence[float],
    zy: Sequence[float],
    harmonic: int = 10
) -> ndarray:
    """
    Compute the Elliptical Fourier Descriptors for a polygon.

    Implements Kuhl and Giardina method of computing the coefficients
    An, Bn, Cn, Dn for a specified number of harmonics. This code is adapted
    from the pyefd module. See the original paper for more detail:

    Kuhl, FP and Giardina, CR (1982). Elliptic Fourier features of a closed
    contour. Computer graphics and image procesnp_sing, 18(3), 236-258.

    Args:
        zx (list): A list (or numpy array) of x coordinate values.
        zy (list): A list (or numpy array) of y coordinate values.
        harmonic (int): The number of harmonics to compute for the given
            shape, defaults to 10.
    Returns:
        numpy.ndarray: A numpy array of shape (harmonics, 4) representing the
        four coefficients for each harmonic computed.
    """
    dxy = diff(array([(x, y) for x, y in zip(zx, zy)]), axis=0)
    dt = sqrt((dxy ** 2).sum(axis=1))
    t = concatenate(([0], cumsum(dt)))
    zt = t[-1]
    phi = (2. * pi * t) / zt
    coeffs = zeros((harmonic, 4))
    for n in range(1, harmonic + 1):
        const = zt / (2 * n * n * pi * pi)
        phi_n = phi * n
        d_np_cos_phi_n = np_cos(phi_n[1:]) - np_cos(phi_n[:-1])
        d_np_sin_phi_n = np_sin(phi_n[1:]) - np_sin(phi_n[:-1])
        a_n = const * np_sum(dxy[:, 1] / dt * d_np_cos_phi_n)
        b_n = const * np_sum(dxy[:, 1] / dt * d_np_sin_phi_n)
        c_n = const * np_sum(dxy[:, 0] / dt * d_np_cos_phi_n)
        d_n = const * np_sum(dxy[:, 0] / dt * d_np_sin_phi_n)
        coeffs[n - 1, :] = a_n, b_n, c_n, d_n
    return coeffs


def fourier_power(
    coeffs: ndarray,
    zx: Sequence[float],
    threshold: float = 0.9999
) -> int:
    """
    Compute the total Fourier power and find the minium number of harmonics
    required to exceed the threshold fraction of the total power.

    This is a good method for identifying the number of harmonics to use to
    describe a polygon. For more details see:

    C. np_costa et al. / Postharvest Biology and Technology 54 (2009) 38-47

    Warning:
        The number of coeffs must be >= the Nyquist Frequency.
    Args:
        coeffs: A numpy array of shape (n, 4) representing the
            four coefficients for each harmonic computed.
        zx: A list (or numpy array) of x coordinate values.
        threshold: The threshold fraction of the total Fourier power,
            the default is 0.9999.
    Returns:
        The number of harmonics required to represent the contour above
        the threshold Fourier power.
    """
    nyq = nyquist(zx)
    total_power = 0
    current_power = 0
    for n in range(nyq):
        total_power += 0.5 * (
            coeffs[n, 0] ** 2 + coeffs[n, 1] ** 2 +
            coeffs[n, 2] ** 2 + coeffs[n, 3] ** 2
        )
    for i in range(nyq):
        current_power += 0.5 * (
            coeffs[i, 0] ** 2 + coeffs[i, 1] ** 2 +
            coeffs[i, 2] ** 2 + coeffs[i, 3] ** 2
        )
        if current_power / total_power > threshold:
            return i + 1
    return nyq


def rotate_contour(
    zx: Sequence[float],
    zy: Sequence[float],
    rotation: float,
    centroid: Tuple[float, float]
) -> Tuple[Sequence[float], Sequence[float]]:
    """
    Rotates a contour about a point by a given amount expressed in degrees.

    Operates by calling rotatePoint() on each x,y pair in turn. X and Y must
    have the same dimensions.

    Args:
        zx: A list (or numpy array) of x coordinate values.
        zy: A list (or numpy array) of y coordinate values.
        rotation: The angle in degrees for the contour to be rotated by.
        centroid: A tuple containing the x,y coordinates of the centroid to
            rotate the contour about.
    Returns:
        A tuple containing a list of x coordinates and a list of y coordinates.
    """
    rxs = []
    rys = []
    for nx, ny in zip(zx, zy):
        rx, ry = _rotate_point((nx, ny), centroid, rotation)
        rxs.append(rx)
        rys.append(ry)
    return rxs, rys


def _rotate_point(
    point: Tuple[float, float],
    center_point: Tuple[float, float],
    angle: float
) -> Tuple[float, float]:
    """
    Rotates a point counter-clockwise around centerPoint.

    The angle to rotate by is supplied in degrees. Code based on:
    https://gist.github.com/somada141/d81a05f172bb2df26a2c

    Args:
        point: The point to be rotated.
        center_point: The point to be rotated about.
        angle: The angle to rotate point by, in the counter-clockwise direction.
    Returns:
        A tuple representing the rotated point.
    """
    angle = radians(angle)
    px, py = point
    cpx, cpy = center_point
    return (
        (px - cpx) * cos(angle) - (py - cpy) * sin(angle) + cpx,
        (px - cpx) * sin(angle) + (py - cpy) * cos(angle) + cpy
    )