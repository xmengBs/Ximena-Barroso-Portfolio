-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 11-06-2025 a las 19:52:23
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `posgrado`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos_doctorado`
--

CREATE TABLE `alumnos_doctorado` (
  `no_CVU` int(6) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Fecha_ingreso` date NOT NULL,
  `Fecha_egreso` date DEFAULT NULL,
  `Fecha_baja` date DEFAULT NULL,
  `documento_baja` varchar(255) DEFAULT NULL,
  `En_tiempo` decimal(3,2) DEFAULT NULL,
  `Fuera_tiempo` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `alumnos_doctorado`
--

INSERT INTO `alumnos_doctorado` (`no_CVU`, `Nombre`, `Fecha_ingreso`, `Fecha_egreso`, `Fecha_baja`, `documento_baja`, `En_tiempo`, `Fuera_tiempo`) VALUES
(49254, 'Picos Ponce Julio Cesar ', '2013-01-25', NULL, NULL, NULL, NULL, NULL),
(215668, 'Cuen Tellez Oswaldo', '2011-08-29', '2015-08-28', NULL, NULL, NULL, NULL),
(240182, 'Corrales Rodriguez Luis Angel', '2012-08-27', '2016-08-26', NULL, NULL, NULL, NULL),
(342806, 'Rodriguez Vega Dora Aydee', '2011-08-29', '2015-08-28', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos_maestria`
--

CREATE TABLE `alumnos_maestria` (
  `no_CVU` int(6) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Fecha_ingreso` date NOT NULL,
  `Fecha_egreso` date DEFAULT NULL,
  `Fecha_baja` date DEFAULT NULL,
  `documento_baja` varchar(255) DEFAULT NULL,
  `En_tiempo` decimal(3,2) DEFAULT NULL,
  `Fuera_tiempo` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `alumnos_maestria`
--

INSERT INTO `alumnos_maestria` (`no_CVU`, `Nombre`, `Fecha_ingreso`, `Fecha_egreso`, `Fecha_baja`, `documento_baja`, `En_tiempo`, `Fuera_tiempo`) VALUES
(1234, 'Jose Noe Audelo Cabanillas', '2026-04-24', NULL, NULL, NULL, NULL, NULL),
(311539, 'Covantes Osuna Cesar ', '2011-08-29', '2013-08-28', NULL, NULL, NULL, NULL),
(352304, 'Covantes Osuna Edgar ', '2011-08-29', '2013-08-28', NULL, NULL, NULL, NULL),
(429104, 'López Barrón Daniel Ernesto', '2011-08-29', NULL, NULL, NULL, NULL, NULL),
(429379, 'Escalante Ruiz Marcia Ekatherine ', '2011-08-29', NULL, NULL, NULL, NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos_doctorado`
--
ALTER TABLE `alumnos_doctorado`
  ADD PRIMARY KEY (`no_CVU`);

--
-- Indices de la tabla `alumnos_maestria`
--
ALTER TABLE `alumnos_maestria`
  ADD PRIMARY KEY (`no_CVU`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
