-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `home_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `expenses_pro`
--

CREATE TABLE `expenses_pro` (
  `id` int(11) NOT NULL,
  `expense_date` date DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_mode` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `expenses_pro`
--

INSERT INTO `expenses_pro` (`id`, `expense_date`, `category`, `description`, `amount`, `payment_mode`) VALUES
(17, '2018-12-14', 'Alcohol', '5 Bottle', 180.00, 'credit card'),
(19, '2025-08-09', 'Alcohol', 'ALcohol', 100.00, 'credit card'),
(20, '2025-04-07', 'Entertainment', 'movie', 44.00, 'other'),
(21, '2025-03-07', 'Groceries', 'Banana', 6.00, 'debit card'),
(22, '2025-08-08', 'Healthcare', 'Medicine', 780.00, 'cash'),
(23, '2025-04-04', 'Housing', 'Rent', 7000.00, 'cash'),
(24, '2025-10-04', 'Transportation', 'travel', 1500.00, 'credit card'),
(25, '2025-04-07', 'Education', 'Books', 1400.00, 'online'),
(26, '2025-04-12', 'Transportation', 'O', 78000.00, 'debit card'),
(27, '2025-04-01', 'Alcohol', 'N', 20000.00, 'credit card');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `expenses_pro`
--
ALTER TABLE `expenses_pro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `expenses_pro`
--
ALTER TABLE `expenses_pro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
