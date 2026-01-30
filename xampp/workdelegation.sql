-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2026 at 11:47 AM
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
(6, 'EMBED0006', '0', 'B.Tech', 'C,C  ,JAVA,Python, Dot Net', '964281822', 'Kommadi Village, Road, Chaitanya Valley, Madhurawada, Visakhapatnam, Andhra Pradesh 530048', 'fc3f5b0c-49ec-4de6-af09-d021c430e848.jpg'),
(7, 'EMBED0007', '4', 'B.Tech', 'Manual and Auto machine', '9908576570', 'Gajuwaka', '76c97087-804c-460f-bc9c-a1f0904e2e2f.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_fw_info`
--

CREATE TABLE `tbl_fw_info` (
  `id` int(11) NOT NULL,
  `xpr` varchar(5) NOT NULL,
  `mb_ble` varchar(5) NOT NULL,
  `flex_max` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_fw_info`
--

INSERT INTO `tbl_fw_info` (`id`, `xpr`, `mb_ble`, `flex_max`) VALUES
(1, '4.66', '5.38', '1.38');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_module_info`
--

CREATE TABLE `tbl_module_info` (
  `id` int(11) NOT NULL,
  `opti_server` varchar(10) NOT NULL,
  `cada` varchar(10) NOT NULL,
  `amp_android` varchar(10) NOT NULL,
  `amp_ios` varchar(10) NOT NULL,
  `msam` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_module_info`
--

INSERT INTO `tbl_module_info` (`id`, `opti_server`, `cada`, `amp_android`, `amp_ios`, `msam`) VALUES
(1, '26.01.03', '26.01.01', '25.12.01', '24.10.01', '26.01.01');

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
(6, 'EMBED0006', '2', 'ravi', 'gAAAAABlxfsO6ChL0HQUfst1FULTgVpccc87kJC7n6Vd1Vk08yUzrv-_hoa7sC_XVzZpZVGvrXHq84GG4J7RrDSUk_QGpKIw2A==', 'ravi@gmail.com', '2024-02-09 15:44:38', '', '', '', '0'),
(7, 'EMBED0007', '3', 'pavan', 'gAAAAABpevuSJzoUZhp1H5wBwpAzx7eLU9yroXAm4n22DnUpJG_Q8oKLq0wlxOWUKFk_Tee3Hn8P80m79d6VngcFDj2FUlVd-w==', 'pavan@gmail.com', '2026-01-29 11:47:54', '', '', '', '0');

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
(1, 'MSAM', 'Vue JS, Ionic Vue', 'Python FastAPI', 'MySQL', 'VS code, PyCharm', '0');

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
(3, 'EMBED0003', '1'),
(4, 'EMBED0004', '1'),
(5, 'EMBED0005', '1'),
(6, 'EMBED0006', '1'),
(7, 'EMBED0007', '1');

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

-- --------------------------------------------------------

--
-- Table structure for table `tbl_tool_headers`
--

CREATE TABLE `tbl_tool_headers` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_tool_headers`
--

INSERT INTO `tbl_tool_headers` (`id`, `name`) VALUES
(3, 'MSAM Keys');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_tool_header_items`
--

CREATE TABLE `tbl_tool_header_items` (
  `id` int(11) NOT NULL,
  `header_id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `value` text NOT NULL,
  `is_copy` tinyint(4) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_tool_header_items`
--

INSERT INTO `tbl_tool_header_items` (`id`, `header_id`, `label`, `value`, `is_copy`) VALUES
(3, 3, 'app_key', 'Application Key (For FUOTA)', 1);

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
-- Indexes for table `tbl_fw_info`
--
ALTER TABLE `tbl_fw_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_module_info`
--
ALTER TABLE `tbl_module_info`
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
-- Indexes for table `tbl_tool_headers`
--
ALTER TABLE `tbl_tool_headers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `tbl_tool_header_items`
--
ALTER TABLE `tbl_tool_header_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `header_id` (`header_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_build_info`
--
ALTER TABLE `tbl_build_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_child`
--
ALTER TABLE `tbl_child`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbl_fw_info`
--
ALTER TABLE `tbl_fw_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_module_info`
--
ALTER TABLE `tbl_module_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_parent`
--
ALTER TABLE `tbl_parent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbl_products_info`
--
ALTER TABLE `tbl_products_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_prod_idx`
--
ALTER TABLE `tbl_prod_idx`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbl_task_info`
--
ALTER TABLE `tbl_task_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_tool_headers`
--
ALTER TABLE `tbl_tool_headers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_tool_header_items`
--
ALTER TABLE `tbl_tool_header_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_tool_header_items`
--
ALTER TABLE `tbl_tool_header_items`
  ADD CONSTRAINT `tbl_tool_header_items_ibfk_1` FOREIGN KEY (`header_id`) REFERENCES `tbl_tool_headers` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
