/*
Navicat MySQL Data Transfer

Source Server         : zipkin
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : zipkin

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-05-03 09:36:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for active_internet_connection
-- ----------------------------
DROP TABLE IF EXISTS `active_internet_connection`;
CREATE TABLE `active_internet_connection` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `proto` varchar(4) NOT NULL,
  `recvq` int(10) unsigned NOT NULL,
  `sendq` int(10) unsigned NOT NULL,
  `localip` varchar(16) NOT NULL,
  `localport` int(10) unsigned NOT NULL,
  `foreignip` varchar(16) NOT NULL,
  `foreignport` int(10) unsigned NOT NULL,
  `state` varchar(12) NOT NULL,
  `pid` int(11) unsigned DEFAULT NULL,
  `progname` varchar(20) DEFAULT NULL,
  `timestamp` bigint(11) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131503 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of active_internet_connection
-- ----------------------------

-- ----------------------------
-- Table structure for hdisk
-- ----------------------------
DROP TABLE IF EXISTS `hdisk`;
CREATE TABLE `hdisk` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `ip` varchar(16) NOT NULL,
  `filesystem` varchar(255) NOT NULL,
  `type` varchar(10) NOT NULL,
  `blocks_byte` bigint(20) unsigned NOT NULL,
  `used` bigint(20) unsigned NOT NULL,
  `available` bigint(20) unsigned NOT NULL,
  `capacity` varchar(5) NOT NULL,
  `mounted_on` varchar(255) NOT NULL,
  `timestamp` bigint(11) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=673 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hdisk
-- ----------------------------

-- ----------------------------
-- Table structure for memory
-- ----------------------------
DROP TABLE IF EXISTS `memory`;
CREATE TABLE `memory` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `ip` text NOT NULL,
  `total` bigint(20) unsigned NOT NULL,
  `used` bigint(20) unsigned NOT NULL,
  `free` bigint(20) unsigned NOT NULL,
  `shared` bigint(20) unsigned NOT NULL,
  `buffers` bigint(20) unsigned NOT NULL,
  `cached` bigint(20) unsigned NOT NULL,
  `minus_buffers_cache_used` bigint(20) unsigned NOT NULL,
  `plus_buffers_cache_free` bigint(20) unsigned NOT NULL,
  `swap_total` bigint(20) unsigned NOT NULL,
  `swap_used` bigint(20) unsigned NOT NULL,
  `swap_free` bigint(20) unsigned NOT NULL,
  `timestamp` bigint(11) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of memory
-- ----------------------------

-- ----------------------------
-- Table structure for ps
-- ----------------------------
DROP TABLE IF EXISTS `ps`;
CREATE TABLE `ps` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `localip` varchar(16) NOT NULL,
  `user` varchar(65) NOT NULL,
  `pid` int(11) unsigned NOT NULL,
  `cpu` float(4,1) unsigned DEFAULT NULL,
  `mem` float(4,1) unsigned DEFAULT NULL,
  `vsz` int(10) unsigned DEFAULT NULL,
  `rss` int(10) unsigned DEFAULT NULL,
  `tty` varchar(16) NOT NULL,
  `stat` varchar(16) DEFAULT NULL,
  `start` varchar(16) NOT NULL,
  `time` varchar(16) NOT NULL,
  `command` varchar(4096) NOT NULL,
  `timestamp` bigint(11) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70431 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ps
-- ----------------------------
