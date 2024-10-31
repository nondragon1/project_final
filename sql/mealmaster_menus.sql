-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 54.169.211.200:3306
-- Generation Time: Oct 14, 2024 at 07:16 PM
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
-- Table structure for table `mealmaster_menus`
--

CREATE TABLE `mealmaster_menus` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `label` longtext NOT NULL,
  `url_resource` longtext NOT NULL DEFAULT (_utf8mb3''),
  `calorie` int NOT NULL,
  `url_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mealmaster_menus`
--

INSERT INTO `mealmaster_menus` (`id`, `name`, `label`, `url_resource`, `calorie`, `url_image`) VALUES
(1, 'แกงเขียวหวานไก่', '00', 'https://thainipponfoods.com/wp-content/uploads/2022/01/3_Chicken-green-curry_267x208_2.jpg', 240, '0.png'),
(2, 'แกงเทโพ', '01', 'https://www.veganlokaa.com/wp-content/uploads/2023/11/tepo-curry-vegan-vegetarian-thai-recipe-1.jpg', 300, '1.png'),
(3, 'แกงเลียง', '02', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBW8boha50Ll7eDX9kftdLLoYulg_VHGY6YA&s', 115, '2.png'),
(4, 'แกงจืดเต้าหู้หมูสับ', '03', 'https://img.wongnai.com/p/1920x0/2019/03/25/16be129786034c1185c4cc0768f61356.jpg', 110, '3.png'),
(5, 'แกงจืดมะระยัดไส้', '04', 'https://p16-va.lemon8cdn.com/tos-alisg-v-a3e477-sg/oYmGEQYPxBEsBvAZAIi7B2yADeSgxCHeIHvQii~tplv-tej9nj120t-origin.webp', 90, '4.png'),
(6, 'แกงมัสมั่นไก่', '05', 'https://img-global.cpcdn.com/recipes/c61520fb2c009617/680x482cq70/%E0%B8%A3%E0%B8%9B-%E0%B8%AB%E0%B8%A5%E0%B8%81-%E0%B8%82%E0%B8%AD%E0%B8%87-%E0%B8%AA%E0%B8%95%E0%B8%A3-%E0%B9%81%E0%B8%81%E0%B8%87%E0%B8%A1%E0%B8%AA%E0%B8%A1%E0%B8%99%E0%B9%84%E0%B8%81.jpg', 325, '5.png'),
(7, 'แกงส้มกุ้ง', '06', 'https://img.wongnai.com/p/1920x0/2018/12/17/bf69cc77dfb94a5ab6df20ffb0622cd2.jpg', 105, '6.png'),
(8, 'ไก่ผัดเม็ดมะม่วงหิมพานต์', '07', 'https://img.wongnai.com/p/1920x0/2021/09/24/6d12a87189264f54a2e5232187a2e6dd.jpg', 335, '7.png'),
(9, 'ไข่เจียว', '08', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsxaGosS-Y98xdGqUUZy-4yxC1ARbiS-cfVw&s', 215, '8.png'),
(10, 'ไข่ดาว', '09', 'https://www.sgethai.com/wp-content/uploads/2023/08/AnyConv.com__42-4-1.webp', 215, '9.png'),
(11, 'ไข่พะโล้', '10', 'https://food.mthai.com/app/uploads/2016/02/phalo.jpg', 210, '10.png'),
(12, 'ไข่ลูกเขย', '11', 'https://s.isanook.com/wo/0/ud/13/68865/68865-thumbnail.jpg', 205, '11.png'),
(13, 'กล้วยบวชชี', '12', 'https://www.khaosod.co.th/wpapp/uploads/2019/03/1-%E0%B9%84%E0%B8%94%E0%B8%84%E0%B8%B1%E0%B8%95-696x592.jpg', 152, '12.png'),
(14, 'ก๋วยเตี๋ยวคั่วไก่', '13', 'https://img.wongnai.com/p/1920x0/2019/06/17/52f225b766a946d89edbf34c98620bba.jpg', 435, '13.png'),
(15, 'กะหล่ำปลีผัดน้ำปลา', '14', 'https://s.isanook.com/wo/0/ud/33/166929/f.jpg?ip/resize/w850/q80/jpg', 230, '14.png'),
(16, 'กุ้งแม่น้ำเผา', '15', 'https://food.mthai.com/app/uploads/2014/08/201.jpg', 99, '15.png'),
(17, 'กุ้งอบวุ้นเส้น', '16', 'https://s359.kapook.com/pagebuilder/341d815e-38d5-4a50-8ba8-3df0d5850f32.jpg', 300, '16.png'),
(18, 'ขนมครก', '17', 'https://thairice.org/wp-content/uploads/2020/06/%E0%B8%82%E0%B8%99%E0%B8%A1%E0%B8%84%E0%B8%A3%E0%B8%81-1.jpg', 92, '17.png'),
(19, 'ข้าวเหนียวมะม่วง', '18', 'https://arit.kpru.ac.th/ap2/local/contents/Food_kpp/thumbs/thumb_40.webp', 350, '18.png'),
(20, 'ข้าวขาหมู', '19', 'https://img-global.cpcdn.com/recipes/san9n06rrmbygemguo0x/680x482cq70/%E0%B8%A3%E0%B8%9B-%E0%B8%AB%E0%B8%A5%E0%B8%81-%E0%B8%82%E0%B8%AD%E0%B8%87-%E0%B8%AA%E0%B8%95%E0%B8%A3-%E0%B8%82%E0%B8%B2%E0%B8%A7%E0%B8%82%E0%B8%B2%E0%B8%AB%E0%B8%A1.jpg', 690, '19.png'),
(21, 'ข้าวคลุกกะปิ', '20', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5ErKKPp7KUFcM6vK8DnFDcUZu1SmjVrwZAQ&s', 410, '20.png'),
(22, 'ข้าวซอยไก่', '21', 'https://img-global.cpcdn.com/recipes/e92bbf51c8601f1b/400x400cq70/photo.jpg', 395, '21.png'),
(23, 'ข้าวผัด', '22', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUZ0a-ztKPMzkd_u8ObLcVJ-lW1pcVdIRw8w&s', 561, '22.png'),
(24, 'ข้าวผัดกุ้ง', '23', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSooDk4v2Gm378LDZ1SL4gGRXI0nkQUo55dsQ&s', 595, '23.png'),
(25, 'ข้าวมันไก่', '24', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6q9Q0nG6nTYI6K9jTAXK0GpJtQ0wtQ_8hYw&s', 596, '24.png'),
(26, 'ข้าวหมกไก่', '25', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhX5nXPvcRQOZlR26FKoP9lT7i3itiTSV7TQ&s', 580, '25.png'),
(27, 'ต้มข่าไก่', '26', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnfvaR2IBCgrWeLSAvRSDPjSM_NdnVNiR7Eg&s', 210, '26.png'),
(28, 'ต้มยำกุ้ง', '27', 'https://img.wongnai.com/p/1920x0/2017/10/19/75678af28e394fbfb473fa1b417a62fc.jpg', 873, '27.png'),
(29, 'ทอดมัน', '28', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmrMUAcg2vk8eDTK2f5_nRhMDpPFYm7obHVA&s', 230, '28.png'),
(30, 'ปอเปี๊ยะทอด', '29', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8C_8QnD5MNOO0gQ1kYUwj8STH3vNlwl5Chw&s', 39, '29.png'),
(31, 'ผักบุ้งไฟแดง', '30', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8bW0SNzp0xNPwUHoJCkFPcfL_-9aNAquLaA&s', 210, '30.png'),
(32, 'ผัดไท', '31', 'https://images.deliveryhero.io/image/foodpanda/recipes/pad-thai.jpg', 486, '31.png'),
(33, 'ผัดกะเพรา', '32', 'https://www.sgethai.com/wp-content/uploads/2023/05/AnyConv.com__86-3.webp', 580, '32.png'),
(34, 'ผัดซีอิ๊วเส้นใหญ่', '33', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwlPVY5t7TnosgmDEV0GLCrtEQCaY50nIoow&s', 679, '33.png'),
(35, 'ผัดฟักทองใส่ไข่', '34', 'https://s359.kapook.com/pagebuilder/08b36989-b21a-4554-b944-746de0beb51b.jpg', 224, '34.png'),
(36, 'ผัดมะเขือยาวหมูสับ', '35', 'https://img.wongnai.com/p/1968x0/2019/04/30/84ebebbe25114ee084d95153eaa2d7ec.jpg', 210, '35.png'),
(37, 'ผัดหอยลาย', '36', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvOqmzfTALYyjp3eqQwtPq7vzTbyYoYCGs8Q&s', 350, '36.png'),
(38, 'ฝอยทอง', '37', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1UZIszrt0LXLcQtTTxtjJQHgL7osXBXjqYA&s', 146, '37.png'),
(39, 'พะแนงไก่', '38', 'https://www.matichonweekly.com/wp-content/uploads/2020/03/%E0%B8%AD%E0%B8%B21.jpg', 230, '38.png'),
(40, 'ยำถั่วพู', '39', 'https://img.wongnai.com/p/1920x0/2018/06/20/a545c8b5c4bc46dea7f1843fb9dab924.jpg', 185, '39.png'),
(41, 'ยำวุ้นเส้น', '40', 'https://img-global.cpcdn.com/recipes/cafa5a3d2de3745f/680x482cq70/%E0%B8%A3%E0%B8%9B-%E0%B8%AB%E0%B8%A5%E0%B8%81-%E0%B8%82%E0%B8%AD%E0%B8%87-%E0%B8%AA%E0%B8%95%E0%B8%A3-%E0%B8%A2%E0%B8%B3%E0%B8%A7%E0%B8%99%E0%B9%80%E0%B8%AA%E0%B8%99%E0%B8%97%E0%B8%B0%E0%B9%80%E0%B8%A5.jpg', 120, '40.png'),
(42, 'ลาบหมู', '41', 'https://www.sgethai.com/wp-content/uploads/2022/08/Image10-2.webp', 119, '41.png'),
(43, 'สังขยาฟักทอง', '42', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRc6e6lnogHj6XlL-dC9E0l1GgSB5j8g3opHw&s', 288, '42.png'),
(44, 'สาคูไส้หมู', '43', 'https://img.wongnai.com/p/1920x0/2019/10/23/99f9e56eaacd4adbbeba5ad134f07eab.jpg', 51, '43.png'),
(45, 'ส้มตำ', '44', 'https://images.deliveryhero.io/image/foodpanda/recipes/green-papaya-salad.jpg', 55, '44.png'),
(46, 'หมูปิ้ง', '45', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5JUPIcKmo3vTv87HIqAFAxUS4LtAvYoSiPg&s', 125, '45.png'),
(47, 'หมูสะเต๊ะ', '46', 'https://img.wongnai.com/p/1920x0/2018/10/31/52a20e563de44402b0ea7483039cd3db.jpg', 345, '46.png'),
(48, 'ห่อหมก', '47', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSxfDOUrmTZPomEN6OvT7D0NC35iMCGkcXEQ&s', 500, '47.png'),
(49, 'ข้าว', '48', '/media/thaimenu/rice.jpg', 1.3, 'rice.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mealmaster_menus`
--
ALTER TABLE `mealmaster_menus`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mealmaster_menus`
--
ALTER TABLE `mealmaster_menus`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
