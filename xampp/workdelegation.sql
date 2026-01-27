-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2026 at 09:22 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `workdelegation`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_build_info`
--

CREATE TABLE `tbl_build_info` (
  `id` int(11) NOT NULL,
  `product_id` varchar(3) NOT NULL,
  `build_date` varchar(19) NOT NULL,
  `version` varchar(8) NOT NULL,
  `build_name` varchar(30) NOT NULL,
  `build_type` enum('0','1') NOT NULL,
  `build_option` enum('0','1') NOT NULL,
  `fixed_list` text NOT NULL,
  `build_path` text NOT NULL,
  `build_status` enum('0','1','2') NOT NULL,
  `remark` text NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `updated_by` varchar(30) NOT NULL,
  `updated_at` varchar(19) NOT NULL,
  `status` enum('0','1') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_build_info`
--

INSERT INTO `tbl_build_info` (`id`, `product_id`, `build_date`, `version`, `build_name`, `build_type`, `build_option`, `fixed_list`, `build_path`, `build_status`, `remark`, `created_by`, `updated_by`, `updated_at`, `status`) VALUES
(1, '3', '2024-11-18 09:59:27', '01.06.23', 'Opti-Trace Server/Dongle_v 23.', '1', '1', 'Released on  \nThu, Jun 1, 2023, 7:06 PM', 'CADA-Demo-SD-Image-01-06-2023.img', '2', '', 'ravi', 'ravi', '2024-11-18 10:11:33', '0'),
(2, '3', '2024-11-18 10:01:48', '02.02.24', 'CADA Server Image (02-02-2024)', '1', '1', 'Released on Mon, Feb 5, 5:26 PM', 'CADA Image', '2', '', 'ravi', 'ravi', '2024-11-18 10:12:35', '0'),
(3, '3', '2024-11-18 10:02:41', '03.06.24', 'New CADA Image with latest CAD', '1', '1', 'Released on \nTue, Jun 4, 8:55 AM\n', 'CADA_PRODUCTION(03-06-2024).img', '2', 'Use this image for testing and for development purposes.', 'ravi', 'ravi', '2024-11-18 10:13:49', '0'),
(4, '3', '2024-11-18 10:03:46', '10.06.24', 'Latest CADA Image 10-06-2024', '1', '1', 'Released on Mon, Jun 10, 9:20 PM\n', 'CADA_PRODUCTION(10-06-2024).img', '0', 'The latest Dongle package is included in this image file.', 'ravi', 'ravi', '2024-11-23 09:23:22', '0'),
(5, '3', '2024-11-18 10:15:58', '29.08.24', 'opti-Trace_APK, CADA Image and', '1', '1', 'Note: Please upgrade Dongle_Ver_24.08.02 and then upgrade CADA_BT_Ver_24.08.02.', ': CADA_PRODUCTION(29-08-2024).img', '1', '', 'ravi', 'ravi', '2024-11-18 10:17:22', '0'),
(6, '1', '2026-01-27 08:47:27', '26.01.01', 'Loraweb', '1', '0', '* New changes updated.', '/desktop', '1', '', 'ravi', '', '', '0');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_child`
--

CREATE TABLE `tbl_child` (
  `id` int(11) NOT NULL,
  `emp_id` varchar(10) NOT NULL,
  `job_role` enum('0','1','2','3','4') NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `skills` varchar(250) NOT NULL,
  `phoneno` varchar(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `photo` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_child`
--

INSERT INTO `tbl_child` (`id`, `emp_id`, `job_role`, `qualification`, `skills`, `phoneno`, `address`, `photo`) VALUES
(1, 'EMBED0001', '', '', '', '', '', ''),
(2, 'EMBED0002', '', '', '', '', '', ''),
(3, 'EMBED0003', '2', 'B.Tech', 'Core JAVA,React.js,Vue.js,Fast API', '7989586850', '32-28-4/3, Atchyammapeta, Allipuram, Visakhaptnam, 530004.', '245202dc-fd2e-42d3-80b8-5d0020379e8b.jpg'),
(4, 'EMBED0004', '1', 'M.Tech', 'Python, Vue.js', '9542088420', '32-25-15, Atchyammapeta, Allipuram, Visakhaptnam, 530004', '5f144289-f700-471e-bab5-5f1f96b02d94.jpg'),
(5, 'EMBED0005', '4', 'B.Tech', 'Auto machine, Manual Testing', '9849171503', 'Main Road, New Gajuwaka, Gajuwaka, Visakhapatnam, Andhra Pradesh 530026', '081d025e-644a-486e-b204-921391b938c2.jpg'),
(6, 'EMBED0006', '0', 'B.Tech', 'C,C  ,JAVA,Python, Dot Net', '964281822', 'Kommadi Village, Road, Chaitanya Valley, Madhurawada, Visakhapatnam, Andhra Pradesh 530048', 'fc3f5b0c-49ec-4de6-af09-d021c430e848.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_parent`
--

CREATE TABLE `tbl_parent` (
  `id` int(11) NOT NULL,
  `emp_id` varchar(10) NOT NULL,
  `user_role` enum('0','1','2','3') NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `created_at` varchar(19) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `updated_at` varchar(19) NOT NULL,
  `updated_by` varchar(30) NOT NULL,
  `active_status` enum('0','1') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_parent`
--

INSERT INTO `tbl_parent` (`id`, `emp_id`, `user_role`, `username`, `password`, `email`, `created_at`, `created_by`, `updated_at`, `updated_by`, `active_status`) VALUES
(1, 'EMBED0001', '0', 'superadmin', 'gAAAAABlxd08AQyrql85ULV2689PUO8E2DTw0_Z2rieJGNZSeevUBAFLxy3IY3AHm8KlKuI7iKk4LSFMRnbrZj3QIveVpKA8Qw==', '', '', '', '', '', '0'),
(2, 'EMBED0002', '1', 'admin', 'gAAAAABlxehoZF53mmchYSSVCjQpN9H2MQNawBwnFeoQQKpW6oySR1ChCjCqBm_H9tH_zzdhDp_-9NZPkQlvvII7WHNCXIbtRg==', '', '', '', '2024-02-09 14:26:03', '', '0'),
(3, 'EMBED0003', '3', 'suresh', 'gAAAAABlxeoiB_MXuylGAuxddiZ3pPLLagtzu2wmqeQc1PdW8NH2DKyekLpMX4cvEl0mPgMbd7ZCXBHO_7vnErgplgnk50uHXw==', 'suresh@gmail.com', '2024-02-09 14:32:26', '', '', '', '0'),
(4, 'EMBED0004', '3', 'venkat', 'gAAAAABlxesvdE7fhyBBp0igy89OfZ5D-FYyVScJ7C7H6pzdRrr4zL0GiYGMk49yW1CWT4Wgtm9cAhI7qvYbPj0NAbUB27KovA==', 'venkat@gmail.com', '2024-02-09 14:36:55', '', '', '', '0'),
(5, 'EMBED0005', '3', 'sai', 'gAAAAABlxfok1dzNYmnnLCT_m9dt6-epVAFQYdZx03wiVqrPmBciV1agSnYiW1rbC1vrjRenZftvir2eObBDTCkFmtDShhC4ZQ==', 'sai@gmail.com', '2024-02-09 15:40:44', '', '', '', '0'),
(6, 'EMBED0006', '2', 'ravi', 'gAAAAABlxfsO6ChL0HQUfst1FULTgVpccc87kJC7n6Vd1Vk08yUzrv-_hoa7sC_XVzZpZVGvrXHq84GG4J7RrDSUk_QGpKIw2A==', 'ravi@gmail.com', '2024-02-09 15:44:38', '', '', '', '0');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_products_info`
--

CREATE TABLE `tbl_products_info` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `frontend` varchar(30) NOT NULL,
  `backend` varchar(30) NOT NULL,
  `database` varchar(30) NOT NULL,
  `framework` varchar(30) NOT NULL,
  `status` enum('0','1') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_products_info`
--

INSERT INTO `tbl_products_info` (`id`, `name`, `frontend`, `backend`, `database`, `framework`, `status`) VALUES
(1, 'Amplifier', 'Vue.js', 'FAST API', 'Mysql', 'VS Code, Pycharm', '0'),
(2, 'OneApp Enterprise', 'Vue.js', 'Python', 'Mysql', 'VS Code, Pycharm', '0'),
(3, 'CADA Images', 'No Console', 'Script', 'No', 'Any Editor', '0'),
(4, 'MSAM', 'Vue JS, Ionic Vue', 'Python', 'MySQL', 'VS code', '0');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_prod_idx`
--

CREATE TABLE `tbl_prod_idx` (
  `id` int(11) NOT NULL,
  `emp_id` varchar(10) NOT NULL,
  `prod_idx` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_prod_idx`
--

INSERT INTO `tbl_prod_idx` (`id`, `emp_id`, `prod_idx`) VALUES
(1, 'EMBED0001', '1'),
(2, 'EMBED0002', '1'),
(3, 'EMBED0003', '4'),
(4, 'EMBED0004', '1'),
(5, 'EMBED0005', '1'),
(6, 'EMBED0006', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_task_info`
--

CREATE TABLE `tbl_task_info` (
  `id` int(11) NOT NULL,
  `product_id` varchar(3) NOT NULL,
  `emp_id` varchar(10) NOT NULL,
  `task` text NOT NULL,
  `version` varchar(8) NOT NULL,
  `images` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`images`)),
  `assigned_at` varchar(19) NOT NULL,
  `assigned_by` varchar(30) NOT NULL,
  `task_progress` enum('0','1','2') NOT NULL,
  `status` enum('0','1') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_task_info`
--

INSERT INTO `tbl_task_info` (`id`, `product_id`, `emp_id`, `task`, `version`, `images`, `assigned_at`, `assigned_by`, `task_progress`, `status`) VALUES
(1, '3', 'EMBED0004', 'Spin control issue', '10.02.20', '{}', '2024-06-19 13:49:31', 'suresh', '1', '0'),
(2, '3', 'EMBED0005', 'Spin controller issue', '24.09.99', '{\"img1\": \"d2e2b4a9-3327-4009-9a26-83a7343b196c.jpg\"}', '2024-09-19 09:08:07', 'suresh', '1', '0'),
(3, '1', 'EMBED0005', 'Log Errors', '26.01.99', '{\"img1\": \"b628a95d-f440-4b87-8e1a-a864998ca083.jpg\", \"img2\": \"77139f12-2260-482c-a72e-0feb8d66454a.jpg\", \"img3\": \"142f8be1-2f20-42aa-be21-76c18e629d5e.jpg\", \"img4\": \"5b713d01-6a3d-437a-9d85-c9fcf7621fdc.jpg\"}', '2026-01-22 12:08:34', 'suresh', '2', '0'),
(4, '1', 'EMBED0004', 'Spin Control not working', '26.01.98', '{}', '2026-01-27 08:48:57', 'suresh', '1', '0'),
(5, '1', 'EMBED0006', 'FUOTA getting struck.', '26.01.97', '{}', '2026-01-27 08:49:28', 'suresh', '0', '0');

-- --------------------------------------------------------

--
-- Stand-in structure for view `tbl_user_info`
-- (See below for the actual view)
--
CREATE TABLE `tbl_user_info` (
`id` int(11)
,`emp_id` varchar(10)
,`user_role` enum('0','1','2','3')
,`username` varchar(30)
,`password` varchar(100)
,`email` varchar(50)
,`created_at` varchar(19)
,`created_by` varchar(30)
,`updated_at` varchar(19)
,`updated_by` varchar(30)
,`active_status` enum('0','1')
,`job_role` enum('0','1','2','3','4')
,`qualification` varchar(50)
,`skills` varchar(250)
,`phoneno` varchar(10)
,`address` varchar(255)
,`photo` varchar(40)
);

-- --------------------------------------------------------

--
-- Structure for view `tbl_user_info`
--
DROP TABLE IF EXISTS `tbl_user_info`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `tbl_user_info`  AS SELECT `t1`.`id` AS `id`, `t1`.`emp_id` AS `emp_id`, `t1`.`user_role` AS `user_role`, `t1`.`username` AS `username`, `t1`.`password` AS `password`, `t1`.`email` AS `email`, `t1`.`created_at` AS `created_at`, `t1`.`created_by` AS `created_by`, `t1`.`updated_at` AS `updated_at`, `t1`.`updated_by` AS `updated_by`, `t1`.`active_status` AS `active_status`, `t2`.`job_role` AS `job_role`, `t2`.`qualification` AS `qualification`, `t2`.`skills` AS `skills`, `t2`.`phoneno` AS `phoneno`, `t2`.`address` AS `address`, `t2`.`photo` AS `photo` FROM (`tbl_parent` `t1` join `tbl_child` `t2` on(`t1`.`emp_id` = `t2`.`emp_id`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_build_info`
--
ALTER TABLE `tbl_build_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_child`
--
ALTER TABLE `tbl_child`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_parent`
--
ALTER TABLE `tbl_parent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_products_info`
--
ALTER TABLE `tbl_products_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_prod_idx`
--
ALTER TABLE `tbl_prod_idx`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_task_info`
--
ALTER TABLE `tbl_task_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_build_info`
--
ALTER TABLE `tbl_build_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_child`
--
ALTER TABLE `tbl_child`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_parent`
--
ALTER TABLE `tbl_parent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_products_info`
--
ALTER TABLE `tbl_products_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_prod_idx`
--
ALTER TABLE `tbl_prod_idx`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_task_info`
--
ALTER TABLE `tbl_task_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
