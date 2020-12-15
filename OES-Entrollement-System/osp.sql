-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2020 at 04:55 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `osp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(20) NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`) VALUES
(1, 'admindivesh@admin.ac.in', 'onlyadminknows');

-- --------------------------------------------------------

--
-- Table structure for table `availability`
--

CREATE TABLE `availability` (
  `id` int(30) NOT NULL,
  `bloodgroup` varchar(5) NOT NULL,
  `organization` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `Units` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `availability`
--

INSERT INTO `availability` (`id`, `bloodgroup`, `organization`, `address`, `Units`) VALUES
(1, 'A+', 'Blood Organization - Tamilnadu', 'xyz street, abc avenue, Chennai-60079, tamilnadu', 100),
(2, 'B+', 'Michael Jones Pvt. Ltd', '78081 Brandy Park Apt. 840\nDanielberg, WY 13938', 102),
(3, 'O', 'Jonathan Ward Pvt. Ltd', '21361 Jessica Forks Apt. 534\nSouth Elizabethberg, MD 55843', 156),
(4, 'AB-', 'Jacqueline Garcia Pvt. Ltd', '14476 Hall Mountains\nWest Samantha, WV 54823', 42),
(5, 'AB+', 'Michael Li Pvt. Ltd', '7629 Flores Path Suite 940\nLake Danielmouth, NE 65165', 249),
(6, 'O', 'Mary Anderson Pvt. Ltd', '334 Tina Neck Apt. 076\nPort Alisonfort, NE 54773', 121),
(7, 'A-', 'Kenneth Reilly Pvt. Ltd', '00445 Jill Plains Apt. 532\nGreenefurt, AR 65887', 99),
(8, 'O', 'Alexander Davidson Pvt. Ltd', '892 Adam Prairie Suite 044\nStevenport, IA 98577', 25),
(9, 'B', 'Isaac Campbell Pvt. Ltd', '70296 James Flats\nPenabury, MN 98129', 207),
(10, 'B+', 'Mark Vega Pvt. Ltd', '723 Barnes Club Apt. 270\nJoneschester, VT 37453', 160),
(11, 'AB+', 'Mario Mejia Pvt. Ltd', '67159 Garcia Parkways Apt. 759\nNew Andrewchester, NJ 35553', 86),
(12, 'A-', 'Ronald Turner Pvt. Ltd', '56986 Henderson Grove\nWilliamsborough, GA 92643', 25),
(13, 'B', 'Jennifer Hunt Pvt. Ltd', '16742 Todd Islands Suite 327\nNorth Joannchester, VA 68895', 90),
(14, 'B-', 'Molly Johnson Pvt. Ltd', '933 Kyle Road Suite 271\nJonesstad, MI 50785', 20),
(15, 'B-', 'Timothy Walker Pvt. Ltd', '433 Richard Islands Suite 921\nSolisland, OH 42530', 215),
(16, 'A-', 'Rhonda Khan Pvt. Ltd', 'PSC 9762, Box 6486\nAPO AA 90940', 159),
(17, 'B', 'Douglas Curry Pvt. Ltd', '797 Cobb Pass Apt. 581\nNorth Kevinburgh, MO 93049', 241),
(18, 'B+', 'Bradley Walker Pvt. Ltd', '7765 Johnson Junction Apt. 648\nWalterschester, KS 15894', 231);

-- --------------------------------------------------------

--
-- Table structure for table `blood camps`
--

CREATE TABLE `blood camps` (
  `id` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `number` varchar(20) NOT NULL,
  `city` varchar(30) NOT NULL,
  `address` varchar(200) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blood camps`
--

INSERT INTO `blood camps` (`id`, `name`, `email`, `number`, `city`, `address`, `date`, `time`) VALUES
(1, '', '', '', '', '', '', ''),
(2, '', '', '', '', '', '', ''),
(3, '', '', '', '', '', '', ''),
(4, '', '', '', '', '', '', ''),
(5, 'divesh', 'ndiveshjain@gmail.com', '9555212355', 'chennai', '20/34 muthukrishnan street', '20th april 2019', '12pm-4pm'),
(6, 'sdfslfkj', 'ddskj', 'klfdjs', 'fdsj', 'sfdsdj', 'fdsjkdh', 'kjfas'),
(7, 'kfdljfs', 'lkdskfj', 'lkdsf', 'kdkjfls', 'fljks', 'fsdlkjad', 'dfslkja'),
(8, 'sfsjlf', 'a', 'ldsj', 'sdf', 'sd', 'dsjsf', 'dflsjf'),
(9, 'djdslkf', 'fldskjk', 'ljdfa', 'fjldksa', 'ajdfsk', 'dfsdjk', 'dsfjkj'),
(10, 'fjkfsd', 'jfsd', 'jdfskf', 'fsjdk', 'kfsjsd', 'kjfdfsd', 'dfkjsd'),
(11, 'dfjs', 'sdljksf', 'ldfkj', 'jfai', 'kjfh', 'kdfsjsh', 'fdskjs'),
(12, 'fdldkjd', 'dfjl', 'fdlj', 'jfds', 'ldjf', 'lfdkj', 'flkjk'),
(13, 'Steven Hoffman', 'Steven@gmail.com', '3231413424', 'Sotofurt', '06604 Robert Island Suite 341\nLake Jamesberg, WY 47018', '2020-11-18', '12 am to 4 pm'),
(14, 'Robin Henry', 'Robin@gmail.com', '7358182598', 'Port Jeremy', '183 Davis Spurs Suite 200\nKurtfurt, WA 59196', '2020-11-15', '12 am to 4 pm'),
(15, 'Amber Johnson', 'Amber@gmail.com', '5956337680', 'Pierceberg', '719 Mcdonald Brook Apt. 218\nBryanmouth, NJ 71668', '2020-11-18', '12 am to 4 pm'),
(16, 'Susan Lee', 'Susan@gmail.com', '1266395902', 'South Madison', '8051 Anna Forge Apt. 716\nLake Trevorville, PA 11494', '2020-11-18', '12 am to 4 pm'),
(17, 'Brandy Price', 'Brandy@gmail.com', '5697470110', 'Whitefurt', '6910 Tara Trail Suite 966\nCharlesberg, NC 39492', '2020-11-20', '12 am to 4 pm'),
(18, 'Richard Perry', 'Richard@gmail.com', '8994333055', 'Lindsayside', '82103 Janet Summit Apt. 509\nBrandonmouth, NE 58706', '2020-11-23', '12 am to 4 pm'),
(19, 'Christian Ellis', 'Christian@gmail.com', '1625137396', 'Jenniferview', '1228 Mueller Stream\nPaulaborough, IA 59550', '2020-11-21', '12 am to 4 pm'),
(20, 'Shaun Carter', 'Shaun@gmail.com', '9543277585', 'North Victor', '4772 Dylan Alley\nLake Randy, NY 39939', '2020-11-14', '11 am to 3 pm'),
(21, 'Angelica Mills', 'Angelica@gmail.com', '2810119475', 'Mcleanland', '58237 Wright Lakes Suite 592\nEast John, MD 71916', '2020-11-14', '12 am to 4 pm'),
(22, 'Daniel Davis', 'Daniel@gmail.com', '8114082215', 'Hollandfurt', '7498 Colon Valleys Suite 139\nPort Stephanieshire, LA 91156', '2020-11-16', '11 am to 3 pm'),
(23, 'Michelle Chaney', 'Michelle@gmail.com', '1395299926', 'Lake William', '3621 Sawyer Well Suite 257\nTheresaland, HI 43661', '2020-11-16', '12 am to 4 pm'),
(24, 'Aaron Gomez', 'Aaron@gmail.com', '3082324873', 'Annashire', '938 Philip Gateway\nSarahstad, NJ 74646', '2020-11-21', '11 am to 3 pm'),
(25, 'William Reese', 'William@gmail.com', '6621208140', 'New Donald', '358 Tracy Ranch\nJonathonstad, TX 75203', '2020-11-20', '12 am to 4 pm'),
(26, 'Allison Smith', 'Allison@gmail.com', '6226342493', 'Whitneystad', '8349 Carla Freeway Suite 709\nRobertside, GA 98523', '2020-11-16', '11 am to 3 pm'),
(27, 'Philip Vargas', 'Philip@gmail.com', '4853214892', 'South Sarahbury', '2009 David Views\nSeanfort, GA 42145', '2020-11-21', '11 am to 3 pm'),
(28, 'Ashley Henry', 'Ashley@gmail.com', '2999668604', 'Julieton', '187 Shane Station Apt. 015\nNatashaside, IL 92502', '2020-11-20', '12 am to 4 pm'),
(29, 'Rebecca Baker', 'Rebecca@gmail.com', '4121464295', 'West Kenneth', '09797 Stephenson Square Suite 274\nWilliamston, UT 07650', '2020-11-20', '11 am to 3 pm'),
(30, 'Sarah Tapia', 'Sarah@gmail.com', '2231624656', 'Joannemouth', 'PSC 2470, Box 4936\nAPO AA 84478', '2020-11-22', '12 am to 4 pm'),
(31, 'Rebecca Porter', 'Rebecca@gmail.com', '1133048861', 'Lopezbury', '4190 Kennedy Circle\nEast Nathanchester, NV 99218', '2020-11-15', '12 am to 4 pm'),
(32, 'George Brown', 'George@gmail.com', '2708128397', 'Jenkinsmouth', '53929 Howe Ridges\nNew Tracy, MT 84891', '2020-11-20', '12 am to 4 pm');

-- --------------------------------------------------------

--
-- Table structure for table `donors`
--

CREATE TABLE `donors` (
  `id` int(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `number` varchar(20) NOT NULL,
  `bgroup` varchar(20) NOT NULL,
  `address` varchar(300) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `donors`
--

INSERT INTO `donors` (`id`, `name`, `number`, `bgroup`, `address`) VALUES
(1, 'Robert Guzman', '5526913041', 'A-', '0625 Heather Lights Suite 044\nPort Tonyaland, AL 59295'),
(2, 'Alexandra Butler', '9899478186', 'A', 'Unit 2657 Box 4152\nDPO AE 90802'),
(3, 'Helen Mitchell', '6268893009', 'AB-', '327 Lisa Junctions\nDeannaburgh, CA 01879'),
(4, 'Alvin Oconnor', '8321315737', 'O', '54909 Crystal Station\nEast Suzanne, OH 64653'),
(5, 'Danielle Castillo', '7667086028', 'O', '22390 Megan Ferry\nTiffanyland, AR 40719'),
(6, 'Jessica Gregory', '9302041802', 'A+', '85140 Leah Canyon\nAndersonfurt, HI 28688'),
(7, 'Lisa Perez', '9069090413', 'B+', '0102 Gary Run Apt. 068\nSouth Teresa, FL 57863'),
(8, 'Patrick Moore', '6066688017', 'A-', '28643 Sarah Landing\nWest Heatherburgh, WA 64706'),
(9, 'Michael Walker', '3608073052', 'B', '90875 Webster Parkways\nCrossmouth, ID 69477'),
(10, 'Juan Rivera', '9303822334', 'B', '7259 Hammond Fords Suite 015\nBeasleymouth, AR 03524'),
(11, 'Anthony Nguyen', '3415210825', 'A-', '872 Janice Skyway Suite 705\nJefferymouth, DE 92509'),
(12, 'Joseph Miller', '9006906185', 'O', '848 Jeremy Bridge Suite 380\nColemanville, VT 38200'),
(13, 'Sara Hernandez', '1931055468', 'A+', '3011 Sara Spring Apt. 201\nMontoyahaven, NH 65009'),
(14, 'Taylor Peterson', '1630787606', 'B', '916 Lamb Centers\nDebraville, GA 29839'),
(15, 'Charlotte Bowman', '5662083938', 'A-', 'Unit 6448 Box 3015\nDPO AA 37494'),
(16, 'Ryan Bryant', '8375272047', 'B-', '91109 Barrett Spurs\nJillianchester, OK 29742'),
(17, 'James Harvey', '5927407751', 'B+', '50820 Mendoza Ridges Apt. 998\nDianafort, SC 88039'),
(18, 'Ashley Welch', '4401157216', 'A-', '512 Hernandez Roads\nDawnfurt, KS 09800'),
(19, 'Gerald Anderson', '1252456284', 'A+', '244 Michael Crescent Apt. 921\nEast Darrylshire, NC 24776'),
(20, 'James Walker', '6377904684', 'B+', 'Unit 3739 Box 0498\nDPO AE 05475'),
(21, 'James Lester', '9950240087', 'AB+', '81550 Robert Crescent Apt. 892\nKhantown, AZ 88676');

-- --------------------------------------------------------

--
-- Table structure for table `organization`
--

CREATE TABLE `organization` (
  `id` int(20) NOT NULL,
  `name` text NOT NULL,
  `city` varchar(30) NOT NULL,
  `address` varchar(200) NOT NULL,
  `number` varchar(15) NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `organization`
--

INSERT INTO `organization` (`id`, `name`, `city`, `address`, `number`, `email`, `password`) VALUES
(1, 'SS org', 'chennai', '20/34 muthukrishnan street, Kondithope, Chennai-600079', '9043926652', 'ssorg@gmail.com', 'ssjain'),
(2, 'hadakarnataka', 'banglore', 'karnataka', '558524422', 'ldksfja@sjdkl.com', 'divehs'),
(3, 'divesh', 'chennai', '20/34 ddd streetq', '99884523855', 'divesh@gmail.com', 'divesh'),
(4, 'manan', 'chesa', 'klasdjf', '988', 'manan@gmail.com', 'manan'),
(5, 'Aaron Mendoza', 'Dustinstad', '384 Christina Corner Apt. 609\nLukemouth, DC 93210', '4486557882', 'Aaron@gmail.com', 'Aaron5021'),
(6, 'Nicholas Taylor', 'North Michael', '725 Riley Plaza Apt. 762\nChristyburgh, ND 07799', '2967935662', 'Nicholas@gmail.com', 'Nicholas1028'),
(7, 'Shawn Harris', 'East Craigside', '37789 Schroeder Streets\nMaxwellton, MS 85367', '9739609484', 'Shawn@gmail.com', 'Shawn6140'),
(8, 'Elizabeth Harris Pvt. Ltd', 'Karaburgh', '543 Thomas Prairie Suite 946\nAguilarchester, GA 41729', '5502871570', 'Elizabeth@gmail.com', 'Elizabeth4113'),
(9, 'Grace Gibson Pvt. Ltd', 'Lake Derek', '89120 Wu Well\nLake William, AR 03766', '3419900622', 'Grace@gmail.com', 'Grace8295'),
(10, 'Amanda Kirby Pvt. Ltd', 'West Lisa', '54973 Brandy Ports\nHodgeview, IA 04891', '2926469607', 'Amanda@gmail.com', 'Amanda1416'),
(11, 'Brian Moore Pvt. Ltd', 'West Jeffrey', '925 Garcia Harbors Apt. 110\nSouth Heatherberg, OR 56464', '4245169909', 'Brian@gmail.com', 'Brian3044'),
(12, 'Stephanie Cole Pvt. Ltd', 'Ramirezville', '838 Lopez Summit Suite 102\nNatalieton, MS 35899', '6317025947', 'Stephanie@gmail.com', 'Stephanie5313'),
(13, 'Nancy Ford Pvt. Ltd', 'West Christopher', '12749 Gilbert Wall Apt. 834\nBrianchester, AK 51208', '7229307648', 'Nancy@gmail.com', 'Nancy3352'),
(14, 'Steven Watson Pvt. Ltd', 'Cartermouth', '2854 Shawn Lodge\nNew Deborahstad, NC 04887', '5748196559', 'Steven@gmail.com', 'Steven2395'),
(15, 'Eric Reed Pvt. Ltd', 'New Logan', 'PSC 3916, Box 3572\nAPO AA 88249', '4920931439', 'Eric@gmail.com', 'Eric1826'),
(16, 'Destiny Young Pvt. Ltd', 'East Timothyberg', '299 Peter Crossing Suite 260\nReynoldsbury, LA 29936', '4147439121', 'Destiny@gmail.com', 'Destiny5080'),
(17, 'Martha Cantrell Pvt. Ltd', 'South Tammy', '6456 Crawford Place Suite 976\nNorth Stephanieview, HI 22691', '6983106975', 'Martha@gmail.com', 'Martha4860'),
(18, 'John Lee Pvt. Ltd', 'Jaredton', '54102 Harris Parkways\nPort Jenniferport, WA 40685', '8816119996', 'John@gmail.com', 'John3295'),
(19, 'Christopher Meyers Pvt. Ltd', 'Fuentesville', '50569 Williams Courts Suite 225\nDawnhaven, WA 66314', '5290355804', 'Christopher@gmail.com', 'Christopher8143'),
(20, 'Dennis Miller Pvt. Ltd', 'Mitchellstad', '838 Chambers Squares\nPort Emily, HI 49350', '3410814379', 'Dennis@gmail.com', 'Dennis2873'),
(21, 'Carlos Campbell Pvt. Ltd', 'West Cynthia', '8624 Peter Place\nNew Dylanchester, MT 93224', '6040107308', 'Carlos@gmail.com', 'Carlos7294'),
(22, 'Cody Martin Pvt. Ltd', 'Jeremiahfort', '493 John Mews\nJenniferchester, UT 19908', '5834826082', 'Cody@gmail.com', 'Cody8643'),
(23, 'Erica Mccarthy Pvt. Ltd', 'South Kimberly', 'Unit 3174 Box 5010\nDPO AP 26298', '4265092404', 'Erica@gmail.com', 'Erica6844');

-- --------------------------------------------------------

--
-- Table structure for table `sponsers`
--

CREATE TABLE `sponsers` (
  `id` int(20) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sponsers`
--

INSERT INTO `sponsers` (`id`, `name`, `email`, `password`) VALUES
(1, 'rohini', 'rohinim@novisync.com', 'Novi1234'),
(2, 'Lindsey Anderson Pvt. Ltd', 'Lindsey@gmail.com', 'Lindsey7095'),
(3, 'Amanda Hines Pvt. Ltd', 'Amanda@gmail.com', 'Amanda2391'),
(4, 'Keith Jackson Pvt. Ltd', 'Keith@gmail.com', 'Keith9911'),
(5, 'Michael Sheppard Pvt. Ltd', 'Michael@gmail.com', 'Michael7406'),
(6, 'Yolanda Andrade Pvt. Ltd', 'Yolanda@gmail.com', 'Yolanda6126'),
(7, 'Kathy Brown Pvt. Ltd', 'Kathy@gmail.com', 'Kathy2510'),
(8, 'Nicholas Alexander Pvt. Ltd', 'Nicholas@gmail.com', 'Nicholas9617'),
(9, 'Christopher Howard Pvt. Ltd', 'Christopher@gmail.com', 'Christopher6803'),
(10, 'Joseph Parker Pvt. Ltd', 'Joseph@gmail.com', 'Joseph1129'),
(11, 'Pamela Rodriguez Pvt. Ltd', 'Pamela@gmail.com', 'Pamela6851'),
(12, 'Eric Gross Pvt. Ltd', 'Eric@gmail.com', 'Eric1614'),
(13, 'Elizabeth Smith Pvt. Ltd', 'Elizabeth@gmail.com', 'Elizabeth2146'),
(14, 'Warren Fuller Pvt. Ltd', 'Warren@gmail.com', 'Warren5066'),
(15, 'Matthew Richardson Pvt. Ltd', 'Matthew@gmail.com', 'Matthew6554'),
(16, 'Jeanne Mcdaniel Pvt. Ltd', 'Jeanne@gmail.com', 'Jeanne9161'),
(17, 'Mark Kelly Pvt. Ltd', 'Mark@gmail.com', 'Mark2568'),
(18, 'Christopher Simmons Pvt. Ltd', 'Christopher@gmail.com', 'Christopher8002'),
(19, 'Matthew Hansen Pvt. Ltd', 'Matthew@gmail.com', 'Matthew4489'),
(20, 'Robert Hopkins Pvt. Ltd', 'Robert@gmail.com', 'Robert2567'),
(21, 'Dana Ryan Pvt. Ltd', 'Dana@gmail.com', 'Dana6392');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(20) NOT NULL,
  `name` text NOT NULL,
  `state` varchar(20) NOT NULL,
  `bloodgroup` varchar(2) NOT NULL,
  `number` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `state`, `bloodgroup`, `number`, `email`, `password`) VALUES
(2, 'divesh', '', '', '', 'diveshdj92@gmail.com', 'divesh'),
(3, 'divesh', '', '', '', 'divesh@gmail.com', 'divesh'),
(4, 'divesh', '', '', '', 'divesh1dd@gmail.com', 'dddd'),
(5, 'divevsh', '', '', '', 'diveshjain@gmail.com', 'divesh'),
(6, 'divesh', 'tamilnadu', 'A+', '988845238', 'xyz@gmail.ac.in', 'divesh'),
(7, 'diveshlunker', 'haryana', 'A+', '9999*******', 'divevsh@gmail.com', 'divesh'),
(8, 'abhinav', 'uttar pradesh', 'A-', '9555212355', 'hada@gmail.com', 'hada'),
(9, 'divesh', '', '', '98845238555', 'xyzabc1908@gmail.com', 'divesh'),
(10, 'asd', '', '', '9884523855', 'ccd@gmail.com', 'divesh'),
(11, 'diveshlunker', '', '', '6544545546', 'klsajdf@gmail.com', 'divesh'),
(12, 'rohini', 'Maharashtra', 'B+', '9146086451', 'rohinim@novisync.com', 'Novi1234'),
(13, 'rohini', 'Maharashtra', 'B+', '9850639421', 'rohinim@gmail.com', 'Novi1234'),
(14, 'Jonathan Bell', 'Oregon', 'B', '9820187251', 'Jonathan@gmail.com', 'Jonathan6863'),
(15, 'Ann Rogers', 'New York', 'A+', '5393942593', 'Ann@gmail.com', 'Ann2349'),
(16, 'Gary Smith', 'Pennsylvania', 'O', '6947927389', 'Gary@gmail.com', 'Gary8828'),
(17, 'Bridget Jennings', 'New Mexico', 'A+', '6490870935', 'Bridget@gmail.com', 'Bridget1090'),
(18, 'Lisa Cruz', 'North Carolina', 'O', '7056235732', 'Lisa@gmail.com', 'Lisa6241'),
(19, 'Christopher Jones', 'Colorado', 'B-', '2044930565', 'Christopher@gmail.com', 'Christopher5926'),
(20, 'Steven Forbes', 'South Dakota', 'AB', '9550270967', 'Steven@gmail.com', 'Steven1123'),
(21, 'Stacey Flores', 'Idaho', 'A', '6020409961', 'Stacey@gmail.com', 'Stacey9333'),
(22, 'Curtis Terry', 'Colorado', 'A-', '6339215876', 'Curtis@gmail.com', 'Curtis5932'),
(23, 'Ann Myers', 'New Jersey', 'AB', '5837131616', 'Ann@gmail.com', 'Ann5953'),
(24, 'Christopher Madden', 'Nevada', 'AB', '2970875925', 'Christopher@gmail.com', 'Christopher7085'),
(25, 'Scott Frazier', 'Wyoming', 'A-', '1742967746', 'Scott@gmail.com', 'Scott7868'),
(26, 'John Holt', 'Maine', 'A+', '5486634532', 'John@gmail.com', 'John2248'),
(27, 'Margaret Murray', 'North Dakota', 'A-', '5401916604', 'Margaret@gmail.com', 'Margaret6058'),
(28, 'Karina Obrien', 'Utah', 'B', '2473707524', 'Karina@gmail.com', 'Karina6461'),
(29, 'Alexandra Jackson', 'Iowa', 'O', '8750615695', 'Alexandra@gmail.com', 'Alexandra1504'),
(30, 'Gordon Moran', 'New York', 'B+', '5043865445', 'Gordon@gmail.com', 'Gordon1524'),
(31, 'Michael King', 'Illinois', 'A-', '6792073047', 'Michael@gmail.com', 'Michael4529'),
(32, 'Jennifer Tanner', 'New Hampshire', 'AB', '8383614956', 'Jennifer@gmail.com', 'Jennifer9380'),
(33, 'Andrew Castro', 'Wisconsin', 'B', '4134327734', 'Andrew@gmail.com', 'Andrew5918');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `availability`
--
ALTER TABLE `availability`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `blood camps`
--
ALTER TABLE `blood camps`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `donors`
--
ALTER TABLE `donors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `organization`
--
ALTER TABLE `organization`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sponsers`
--
ALTER TABLE `sponsers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `availability`
--
ALTER TABLE `availability`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `blood camps`
--
ALTER TABLE `blood camps`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `donors`
--
ALTER TABLE `donors`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `organization`
--
ALTER TABLE `organization`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `sponsers`
--
ALTER TABLE `sponsers`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
