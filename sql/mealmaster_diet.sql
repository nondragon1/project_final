-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 54.169.211.200:3306
-- Generation Time: Oct 14, 2024 at 07:19 PM
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
-- Table structure for table `mealmaster_diet`
--

CREATE TABLE `mealmaster_diet` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `detail` longtext NOT NULL,
  `menu` json NOT NULL,
  `url` longtext NOT NULL DEFAULT (_utf8mb3'')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mealmaster_diet`
--

INSERT INTO `mealmaster_diet` (`id`, `name`, `detail`, `menu`, `url`) VALUES
(1, 'Ketogenic Diet', 'A high-fat, low-carbohydrate diet that aims to induce a state of ketosis, where\r\nthe body primarily burns fat for energy instead of carbohydrates. It\'s often used for weight loss\r\nand has potential health benefits, including improved blood sugar control and increased\r\nenergy', '[41, 47, 42, 16, 28 , 11]', ''),
(2, 'Atkins Diet', 'A low-carb diet created by Dr. Robert C. Atkins, which promotes weight loss by\r\nreducing carbohydrate intake and increasing fat and protein consumption. It focuses on four\r\nphases, with the early phases being very low in carbs and gradually increasing carb intake as\r\nthe diet progresses.', '[31 , 28 , 9 , 42 , 17]', ''),
(3, 'Paleo Diet', ' Based on the idea of eating like our ancestors, it includes whole foods like lean\r\nmeats, fish, vegetables, and fruits while excluding processed foods, grains, legumes, and dairy.\r\nThe diet aims to mimic the dietary patterns of pre-agricultural humans and is often called the\r\n\"caveman diet.\"', '[45 , 7 , 42 , 41 , 28]', ''),
(4, 'Intermittent Fasting', 'A dietary approach that cycles between periods of fasting and eating,\r\nwith various methods such as the 16/8 method (fasting for 16 hours and eating within an 8-\r\nhour window).\r\nIt may help with weight loss, improve insulin sensitivity, and promote cellular repair.', '[10 , 15 , 31 , 42 , 7]', ''),
(5, 'Basal Metabolic Rate (BMR)', 'The amount of energy or calories your body needs to maintain\r\nbasic functions at rest, such as breathing, circulation, and cell production.\r\nBMR is used to determine daily calorie needs and is influenced by factors like age, gender,\r\nweight, and muscle mass.', '[6, 9, 17, 22, 35, 42, 43]', ''),
(6, 'Mediterranean Diet', 'A diet inspired by the traditional dietary patterns of countries bordering\r\nthe Mediterranean Sea, which includes a balance of fruits, vegetables, whole grains, lean\r\nproteins, and healthy fats (such as olive oil).\r\nIt\'s associated with numerous health benefits, including heart health, reduced risk of chronic\r\ndiseases, and longevity.', '[14 , 16 , 15 , 31 , 17]', ''),
(7, 'Increasing weight', 'This approach involves controlling your caloric intake and\r\nexpenditure to achieve your desired weight outcome, regardless of the specific diet framework.', '[25 , 9 , 13 , 19 , 29]', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mealmaster_diet`
--
ALTER TABLE `mealmaster_diet`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mealmaster_diet`
--
ALTER TABLE `mealmaster_diet`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
