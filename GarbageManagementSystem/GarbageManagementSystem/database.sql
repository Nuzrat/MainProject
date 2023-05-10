/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - lgms
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`lgms` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `lgms`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `Assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `Driver_id` int(11) DEFAULT NULL,
  `Place_id` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`Assign_id`,`Driver_id`,`Place_id`,`Date`,`Status`) values 
(1,2,1,'2023-05-09','pending');

/*Table structure for table `booking_info` */

DROP TABLE IF EXISTS `booking_info`;

CREATE TABLE `booking_info` (
  `Booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `Product_id` int(11) DEFAULT NULL,
  `User_id` int(11) DEFAULT NULL,
  `Quality` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `booking_info` */

/*Table structure for table `camp` */

DROP TABLE IF EXISTS `camp`;

CREATE TABLE `camp` (
  `Camp_id` int(11) NOT NULL AUTO_INCREMENT,
  `Camp` varchar(50) DEFAULT NULL,
  `Camp_details` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Camp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `camp` */

insert  into `camp`(`Camp_id`,`Camp`,`Camp_details`,`Date`) values 
(1,'camp1','20 person can','2023-05-28');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`id`,`uid`,`complaint`,`date`,`reply`) values 
(1,3,'delay','2023-05-09','pending');

/*Table structure for table `driver` */

DROP TABLE IF EXISTS `driver`;

CREATE TABLE `driver` (
  `Driver_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `F_name` varchar(50) DEFAULT NULL,
  `L_name` varchar(50) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Post` varchar(50) DEFAULT NULL,
  `Pin` varchar(50) DEFAULT NULL,
  `Phone` bigint(20) DEFAULT NULL,
  `Email_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Driver_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `driver` */

insert  into `driver`(`Driver_id`,`login_id`,`F_name`,`L_name`,`Place`,`Post`,`Pin`,`Phone`,`Email_id`) values 
(1,2,'nithin','lal','Malappuram','tirurangadi','676306',9878987878,'nithin@gmail.com');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `did` int(11) DEFAULT NULL,
  `lati` float DEFAULT NULL,
  `longi` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`id`,`did`,`lati`,`longi`) values 
(1,11,11.2578,75.7845),
(2,2,11.2578,75.7845);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'nithin','nithin@123','driver'),
(3,'anwar ','anwar','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `Notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `Driver_id` int(11) DEFAULT NULL,
  `Date` varchar(500) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`Notification_id`,`User_id`,`Driver_id`,`Date`,`status`,`notification`) values 
(1,3,2,'2023-05-09','pending','please take soon'),
(2,3,2,'2023-05-09','pending','please take soon'),
(3,3,2,'2023-05-09','pending','ggg');

/*Table structure for table `pickup_notification` */

DROP TABLE IF EXISTS `pickup_notification`;

CREATE TABLE `pickup_notification` (
  `PickUp_id` int(11) NOT NULL AUTO_INCREMENT,
  `Driver_id` int(11) DEFAULT NULL,
  `User_id` int(11) DEFAULT NULL,
  `Date` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`PickUp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `pickup_notification` */

insert  into `pickup_notification`(`PickUp_id`,`Driver_id`,`User_id`,`Date`) values 
(1,2,3,'2023-05-09'),
(2,2,3,'2023-05-09');

/*Table structure for table `places` */

DROP TABLE IF EXISTS `places`;

CREATE TABLE `places` (
  `Place_id` int(11) NOT NULL AUTO_INCREMENT,
  `Place` varchar(50) DEFAULT NULL,
  `Latitude` varchar(50) DEFAULT NULL,
  `Longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Place_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `places` */

insert  into `places`(`Place_id`,`Place`,`Latitude`,`Longitude`) values 
(1,'kuttipuram','10.8423','76.0299');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `Product_id` int(11) NOT NULL AUTO_INCREMENT,
  `Product` varchar(50) DEFAULT NULL,
  `Type` varchar(50) DEFAULT NULL,
  `Image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `product` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) DEFAULT NULL,
  `F_name` varchar(50) DEFAULT NULL,
  `L_name` varchar(50) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Post` varchar(50) DEFAULT NULL,
  `Pin` varchar(50) DEFAULT NULL,
  `Phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`User_id`,`Login_id`,`F_name`,`L_name`,`Place`,`Post`,`Pin`,`Phone`,`email`) values 
(1,3,'Anwar','jan','1','kuttipuram ','676511',9895765432,'jan@gmail.com');

/*Table structure for table `videos` */

DROP TABLE IF EXISTS `videos`;

CREATE TABLE `videos` (
  `Video_id` int(11) NOT NULL AUTO_INCREMENT,
  `Videos` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Video_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `videos` */

insert  into `videos`(`Video_id`,`Videos`) values 
(1,'VID-20230504-WA0001_1.mp4');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
