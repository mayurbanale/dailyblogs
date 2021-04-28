-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2020 at 12:49 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dailyblogs`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` int(10) NOT NULL,
  `Titleheading` varchar(100) NOT NULL,
  `Date` date NOT NULL,
  `Subject` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `Titleheading`, `Date`, `Subject`) VALUES
(1, 'Travel Blogs. ...', '2020-12-01', 'Travel blogs are becoming more popular each day. Due to cheap air travel, people are traveling more than ever, and they are always looking for travel tips, advice, and destination guides.'),
(4, ' Food Blogs', '2020-12-10', 'Food blogs are another popular blog type. It attracts a lot of readers who are interested in recipes, ingredients, healthy eating, fine dining, and other food related stories.'),
(5, 'Music Blogs', '2020-01-31', 'Music blogs has a wide audience who search for critiques on the best and trending music. Music lovers enjoy songs from different languages, cultures and norms.'),
(9, ' Lifestyle Blogs', '2020-12-20', 'Lifestyle blogs are the most popular type of blogs you can find online. They have a variety of readers, interested in topics ranging from culture, arts, local news, and politics. This gives the blogger a wide range of topics to cover, making it easier to plan their content strategy.\r\n\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(11) NOT NULL,
  `User` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Pass` varchar(10) NOT NULL,
  `Cpass` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `User`, `Email`, `Pass`, `Cpass`) VALUES
(3, 'mayur', 'mayurbanale@gmail.com', '12345', 12345);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`Email`),
  ADD KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
