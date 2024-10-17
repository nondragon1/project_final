-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 54.169.211.200:3306
-- Generation Time: Oct 14, 2024 at 07:15 PM
-- Server version: 9.0.1
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webapp_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `mealmaster_category`
--

CREATE TABLE `mealmaster_category` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `menus` json NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mealmaster_category`
--

INSERT INTO `mealmaster_category` (`id`, `name`, `menus`) VALUES
(1, 'Noodles', '[14, 32, 34, 22]'),
(2, 'Sweet Food', '[13, 18, 19, 38, 43, 44]'),
(3, 'Add on', '[49]'),
(4, 'Fast Food', '[9, 10, 17, 33, 37, 42, 45, 46, 47, 3, 4]'),
(5, 'Steak', '[16]'),
(6, 'Snack Food', '[30, 29]'),
(7, 'Clean Food', '[35, 28, 27, 40, 41]'),
(8, 'One Dish Meal', '[23, 24, 25, 21, 26, 22, 20, 19, 8, 1, 2, 5, 6, 7, 11, 12, 39, 48]'),
(9, 'Vegetarian Food', '[15, 36, 31]');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mealmaster_category`
--
ALTER TABLE `mealmaster_category`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mealmaster_category`
--
ALTER TABLE `mealmaster_category`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
