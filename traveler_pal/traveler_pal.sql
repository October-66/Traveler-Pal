-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: traveler_pal
-- ------------------------------------------------------
-- Server version	5.5.46-0ubuntu0.14.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_activity`
--

DROP TABLE IF EXISTS `app_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `launchedDateTime` datetime DEFAULT NULL,
  `startDateTime` datetime DEFAULT NULL,
  `endDateTime` datetime DEFAULT NULL,
  `introduction` varchar(128) NOT NULL,
  `sponsor` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_activity`
--

LOCK TABLES `app_activity` WRITE;
/*!40000 ALTER TABLE `app_activity` DISABLE KEYS */;
INSERT INTO `app_activity` VALUES (1,'12.22北京之旅','2015-12-21 16:00:00','2015-12-21 16:00:00','2015-12-23 16:00:00','一起去北京玩几天，感受社会主义新中国','1111'),(2,'丝路旅痕-河西走廊大暴走','2015-12-23 16:00:00','2015-12-31 16:00:00','2016-01-07 16:00:00','重温丝绸之路，探索先烈遗迹','麦秆吸管'),(3,'再闯河西','2015-12-23 16:00:00','2016-01-04 16:00:00','2016-03-15 16:00:00','上次去河西不过瘾，这次多去几个地方，有愿意的一起走起！','麦秆吸管'),(4,'关东游','2015-12-24 16:00:00','2015-02-14 16:00:00','2015-02-14 16:00:00','谁水水水水水水水水水水水水水水水水水水水水是','1111'),(5,'哈尔滨游','2015-12-24 16:00:00','2015-02-14 16:00:00','2015-02-14 16:00:00','的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶大啥啥啥滴答滴答','1111'),(6,'我爱哈工大','2015-12-24 16:00:00','2015-02-14 16:00:00','2015-02-14 16:00:00','嘿嘿嘿嘿','1111'),(7,'哈工大玩玩玩','2015-12-24 16:00:00','2015-02-14 16:00:00','2015-02-24 16:00:00','哈哈哈哈哈哈，让我们一起摇摆摇摆','1111'),(8,'新疆游玩','2015-12-24 16:00:00','2015-02-14 16:00:00','2015-02-14 16:00:00','','1111'),(9,'去看冰雪大世界','2015-12-24 16:00:00','2015-12-23 16:00:00','2015-02-14 16:00:00','开开心心看哈尔滨看雪','1111');
/*!40000 ALTER TABLE `app_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_activityscenery`
--

DROP TABLE IF EXISTS `app_activityscenery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_activityscenery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity_id` int(11) DEFAULT NULL,
  `scenery_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_activityscenery_activity_id_7c2240c4_fk_app_activity_id` (`activity_id`),
  KEY `app_activityscenery_scenery_id_6f3df77f_fk_app_scenery_id` (`scenery_id`),
  CONSTRAINT `app_activityscenery_activity_id_7c2240c4_fk_app_activity_id` FOREIGN KEY (`activity_id`) REFERENCES `app_activity` (`id`),
  CONSTRAINT `app_activityscenery_scenery_id_6f3df77f_fk_app_scenery_id` FOREIGN KEY (`scenery_id`) REFERENCES `app_scenery` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_activityscenery`
--

LOCK TABLES `app_activityscenery` WRITE;
/*!40000 ALTER TABLE `app_activityscenery` DISABLE KEYS */;
INSERT INTO `app_activityscenery` VALUES (2,1,3),(3,1,4),(4,2,6),(5,3,7),(6,3,8),(7,3,6),(8,3,9),(9,4,10),(10,5,11),(11,5,12),(12,6,13),(13,6,14),(14,7,13),(15,7,14),(16,8,16),(17,8,17),(18,9,11),(19,9,11);
/*!40000 ALTER TABLE `app_activityscenery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_person`
--

DROP TABLE IF EXISTS `app_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `username` varchar(128) DEFAULT NULL,
  `interest` longtext,
  `gender` varchar(1) NOT NULL,
  `userImg` varchar(100) NOT NULL,
  `isroot` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_person`
--

LOCK TABLES `app_person` WRITE;
/*!40000 ALTER TABLE `app_person` DISABLE KEYS */;
INSERT INTO `app_person` VALUES (1,3,'1111','滑冰，洗澡，爬山','M','','Y'),(2,4,'2222',NULL,'M','','N'),(3,5,'4444',NULL,'M','','N'),(4,6,'5555',NULL,'M','','N'),(6,8,'1234','滑冰','M','','N'),(7,9,'gggg',NULL,'M','','N');
/*!40000 ALTER TABLE `app_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_personactivity`
--

DROP TABLE IF EXISTS `app_personactivity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_personactivity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `activity_id` int(11) DEFAULT NULL,
  `joinedDateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_personactivity`
--

LOCK TABLES `app_personactivity` WRITE;
/*!40000 ALTER TABLE `app_personactivity` DISABLE KEYS */;
INSERT INTO `app_personactivity` VALUES (1,6,8,'2015-12-25 03:25:15'),(2,7,9,'2015-12-25 04:14:13');
/*!40000 ALTER TABLE `app_personactivity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_personscenery`
--

DROP TABLE IF EXISTS `app_personscenery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_personscenery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `scenery_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_personscenery`
--

LOCK TABLES `app_personscenery` WRITE;
/*!40000 ALTER TABLE `app_personscenery` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_personscenery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_postable`
--

DROP TABLE IF EXISTS `app_postable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_postable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `title` varchar(128) NOT NULL,
  `content` longtext NOT NULL,
  `postDateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_postable`
--

LOCK TABLES `app_postable` WRITE;
/*!40000 ALTER TABLE `app_postable` DISABLE KEYS */;
INSERT INTO `app_postable` VALUES (4,1,'浅谈表单POST数据的编码方式','<p><br/></p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">在HTTP协议中并没有规定POST请求的数据要采用编码何种方式，从某种程度上说，这种编码方式可以是自定义的，可以是任意的。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">当然，这种编码是需要和服务器有一个合适的约定，这样服务器端才能正确的解码得到的数据。通常来说，服务器是根据request中的header中的Content-Type来获取传送的数据是采用何种编码方式。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">就常见的语言来说，一般会内置下面几个常见编码方式的解析。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"zoom: 1; font-size: 24px;\">1.application/x-www-form-urlencoded</span></p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">在form表单中，默认的情况就是这种enctype属性。也就是说，如果不显式的指定form表单post数据的编码方式的话，就会是以默认的application/x-www-form-urlencoded编码方式传输数据。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">在Jquery中，进行Ajax提交数据的时候默认也是这种编码方式。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"zoom: 1; font-size: 24px;\">2. multipart/form-data</span></p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">这种编码方式也是极其常见的，主要表现在利用表单来传输文件的时候。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">通常是这样书写：</p><pre class=\"brush:html;toolbar:false\" style=\"zoom: 1; padding: 9.5px; font-family: Monaco, Menlo, Consolas, &#39;Courier New&#39;, monospace; font-size: 13px; color: rgb(51, 51, 51); border-radius: 4px; margin-top: 0px; margin-bottom: 10px; line-height: 20px; border: 1px solid rgba(0, 0, 0, 0.14902); white-space: pre-wrap; word-break: break-all; background-color: rgb(245, 245, 245);\">&nbsp;&lt;FORM&nbsp;ENCTYPE=&quot;multipart/form-data&quot;&nbsp;ACTION=&quot;_URL_&quot;&nbsp;METHOD=POST&gt;\r\n&nbsp;&nbsp;&nbsp;&nbsp;File&nbsp;to&nbsp;process:&nbsp;&lt;INPUT&nbsp;NAME=&quot;userfile1&quot;&nbsp;TYPE=&quot;file&quot;&gt;\r\n&nbsp;&nbsp;&nbsp;&nbsp;&lt;INPUT&nbsp;TYPE=&quot;submit&quot;&nbsp;VALUE=&quot;Send&nbsp;File&quot;&gt;\r\n&lt;/FORM</pre><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"zoom: 1; font-size: 24px;\">3. application/json</span></p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">这种编码方式在支持上就没有前面两种强悍了，但由于通常情况下语言对Json的序列化都做的很好，我们可以自行的获取数据流，然后做decode操作就能得到一个json式的对象，极其方便的去进行数据操作。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">当然语言支持不好不代表框架支持也不好，很多主流的框架也已经开始使用这种方式了。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">当然，真心觉得不好用的话也可以把得到的Json数据变成一个字符串，然后用application/x-www-form-urlencoded的方式编码，后台得到后再解析为json对象</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"zoom: 1; font-size: 24px;\">4. text/xml</span></p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\">相比Json而言，他的出现更早，在早期的使用上也更为广泛，各种语言对他的解析也是相当不错。不过近年来的json风也让他有了很大程度上的衰落。</p><p style=\"zoom: 1; margin-top: 0px; margin-bottom: 10px; padding: 0px; text-indent: 2em; color: rgb(68, 68, 68); font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background-color: rgb(255, 255, 255);\"><br style=\"zoom: 1;\"/></p><blockquote style=\"zoom: 1; color: rgb(51, 51, 51); margin: 0px 0px 10px; padding: 10px; border: 1px dashed rgb(222, 222, 222); border-radius: 2px; font-family: 微软雅黑, Tahoma, Helvetica, Arial, SimSun, sans-serif; font-size: 14.4px; line-height: 25.92px; white-space: normal; background: rgb(248, 248, 248);\"><p>转载请注明：<a href=\"http://www.rccoder.net/sitemap\" style=\"zoom: 1; color: rgb(43, 165, 243); text-decoration: none;\">www.rccoder.net|若兮为尘</a><br style=\"zoom: 1;\"/>如果你喜欢本文，或者感觉本文对你有帮助，就点击下面的分享按钮，把这篇文章分享出去吧~</p></blockquote><p><br/></p>','2015-12-23 16:00:00'),(5,1,'大神大神','<p>&nbsp; &nbsp; abc大神大神</p>','2015-02-14 16:00:00'),(6,1,'N+X超级路演”活动圆满结束','<p style=\"white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 43px; color: rgb(64, 64, 64); line-height: 21px; background-color: rgb(255, 255, 255);\"><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">12</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">月</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">21</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">日下午</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">，由校团委、哈工大大学生创新创业园、爱立方联合众创空间、北京恒牛创投和北京光合派联合举办的</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">“N+X</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">超级路演<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">”</span>活动在创新创业园的</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">功夫咖啡</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">成功举办。</span></p><p style=\"white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 43px; color: rgb(64, 64, 64); line-height: 21px; background-color: rgb(255, 255, 255);\"><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">哈药集团原董事长丛国章</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">、</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">哈尔滨市工信委总经济师张国华、哈尔滨市国税局所得税处处长王晓玲、哈尔滨市科技局平台处处长李奇志、北京恒牛创投创始合伙人曹沿松</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">、</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">北京光合派创始合伙人朴俊红</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">、</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">哈以孵化器董事长常舒宇</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">、</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">哈高科董事长李波、</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">科力投资投资副总陈萌</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">、</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">哈创新投投资部长罗智博、天琪资本投资副总费腾、宽带资本高级合伙人于博洋和九鼎投资高级投资经理于颖等作为路演评委出席活动，哈工大校团委副书记李敬伟主持。</span></p><p style=\"white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 43px; color: rgb(64, 64, 64); line-height: 21px; background-color: rgb(255, 255, 255);\"><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">首先，朴俊红</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">女士围绕“商业模式的自我评估”这一话题为参与活动的创业者进行了简明扼要的创业培训。随后，神州城、寻思解题、叮咚学、爱芝兰科技、智慧轮椅、黄桃挖核机器人、爱月宝和<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">91</span>校车等<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">8</span>个在前期经过创业导师仔细打磨辅导的创业项目上台进行路演，各公司负责人从创业项目、市场剖析、融资计划和团队构成等方面进行阐述，路演评委与创业团队就项目的运行现状、商业模式、市场前景等多个方面进行提问和指导。现场观众也与创业团队进行了互动，现场气氛轻松活泼，项目在讨论中得以不断完善和提升。</span></p><p style=\"white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 43px; color: rgb(64, 64, 64); line-height: 21px; background-color: rgb(255, 255, 255);\"><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">在近三个小时的头脑风暴和灵感碰撞后，</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">“N+X</span><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">超级路演<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">”</span>圆满结束，参加路演的创业团队或对自己的项目有了新的灵感和改进方案，或在现场找到了有意向的合作伙伴。寻思解题负责人李享说道：<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">“</span>这样的活动为处于初创期的企业提供了很好的平台和机会，让如此多的投资经理打磨项目，我们获益匪浅，希望园区在未来还可以更多地举办这样的路演活动<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">”</span>。本次路演活动中众多投资人一致看好我校大学生创新创业园在孵企业哈尔滨爱芝兰科技有限公司主营的家用精工自酿啤酒机项目，将在明年初受邀参加<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">“N+X</span>超级路演<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">”</span>北京站的活动，届时将受到<span style=\"box-sizing: border-box; border: 0px; font-size: 21.3333px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline;\">SOHO</span>中国董事长潘石屹在内众多国内顶级企业家和投资人的评审和指导。</span></p><p style=\"white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 43px; color: rgb(64, 64, 64); line-height: 21px; background-color: rgb(255, 255, 255);\"><span style=\"box-sizing: border-box; border: 0px; font-size: 21px; font-style: inherit; font-weight: inherit; outline: 0px; padding: 0px; vertical-align: baseline; line-height: 32px; color: rgb(38, 38, 38);\">活动最后，李敬伟向丛国章董事长等知名企业家和投资人颁发创新创业园创业导师聘书，今后这些导师将定期到园区参加项目路演和一对一辅导，帮助创业园的学生创业企业项目更好发展。</span></p><p style=\"margin-top: 0px; margin-bottom: 0.5em; white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 28px; color: rgb(64, 64, 64); text-align: center; background-color: rgb(255, 255, 255);\"><img width=\"550\" height=\"314\" alt=\"\" src=\"http://today.hit.edu.cn/uploadfiles/2015/12-24/20151224193940.png\" style=\"box-sizing: border-box; height: auto; max-width: 100%;\"/></p><p style=\"margin-top: 0px; margin-bottom: 0.5em; white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 28px; color: rgb(64, 64, 64); text-align: center; background-color: rgb(255, 255, 255);\"><img width=\"550\" height=\"334\" alt=\"\" src=\"http://today.hit.edu.cn/uploadfiles/2015/12-24/20151224194110.png\" style=\"box-sizing: border-box; height: auto; max-width: 100%;\"/></p><p style=\"margin-top: 0px; margin-bottom: 0.5em; white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 28px; color: rgb(64, 64, 64); text-align: center; background-color: rgb(255, 255, 255);\"><img width=\"550\" height=\"755\" alt=\"\" src=\"http://today.hit.edu.cn/uploadfiles/2015/12-24/2015122419455.jpg\" style=\"box-sizing: border-box; height: auto; max-width: 100%;\"/></p><p style=\"margin-top: 0px; margin-bottom: 0.5em; white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 28px; color: rgb(64, 64, 64); text-align: center; background-color: rgb(255, 255, 255);\"><img width=\"550\" height=\"412\" alt=\"\" src=\"http://today.hit.edu.cn/uploadfiles/2015/12-24/20151224194046.jpg\" style=\"box-sizing: border-box; height: auto; max-width: 100%;\"/></p><p style=\"margin-top: 0px; margin-bottom: 0.5em; white-space: normal; box-sizing: border-box; border: 0px; outline: 0px; padding: 0px; vertical-align: baseline; text-indent: 28px; color: rgb(64, 64, 64); text-align: center; background-color: rgb(255, 255, 255);\"><img width=\"550\" height=\"412\" alt=\"\" src=\"http://today.hit.edu.cn/uploadfiles/2015/12-24/20151224193918.jpg\" style=\"box-sizing: border-box; height: auto; max-width: 100%;\"/></p><p style=\"white-space: normal;\"><br/></p><h1 class=\"entry-title\" style=\"box-sizing: border-box; border: 0px; font-family: &#39;Microsoft YaHei&#39;, ÃƒÆ’Ã‚Â¥Ãƒâ€šÃ‚Â¾Ãƒâ€šÃ‚Â®ÃƒÆ’Ã‚Â¨Ãƒâ€šÃ‚Â½Ãƒâ€šÃ‚Â¯ÃƒÆ’Ã‚Â©ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â©Ãƒâ€šÃ‚Â»ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“, &#39;Microsoft JhengHei&#39;, ÃƒÆ’Ã‚Â¥Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â½ÃƒÆ’Ã‚Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ÃƒÆ’Ã‚Â§Ãƒâ€šÃ‚Â»ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â&nbsp;ÃƒÆ’Ã‚Â©Ãƒâ€šÃ‚Â»ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“, STHeiti, MingLiu; margin: 0px; outline: 0px; padding: 0px; vertical-align: baseline; font-size: 25px; color: rgb(64, 64, 64); white-space: normal; background-color: rgb(255, 255, 255);\"><br/></h1>','2015-02-14 16:00:00'),(7,1,'攻略测试','<p>冰雪大世界好没</p>','2015-02-05 16:00:00');
/*!40000 ALTER TABLE `app_postable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_scenery`
--

DROP TABLE IF EXISTS `app_scenery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_scenery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_scenery`
--

LOCK TABLES `app_scenery` WRITE;
/*!40000 ALTER TABLE `app_scenery` DISABLE KEYS */;
INSERT INTO `app_scenery` VALUES (3,'故宫',NULL),(4,'中关村',NULL),(5,'pureweber',NULL),(6,'敦煌',NULL),(7,'兰州',NULL),(8,'瓜州',NULL),(9,'嘉峪关',NULL),(10,'关东',NULL),(11,'哈尔滨中央大街',NULL),(12,'哈尔滨格林公园',NULL),(13,'哈工大一校区',NULL),(14,'哈工大二校区',NULL),(15,'啥啥啥',NULL),(16,'乌鲁木齐',NULL),(17,'塔克拉玛干',NULL),(18,'冰雪大世界',NULL);
/*!40000 ALTER TABLE `app_scenery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_slider`
--

DROP TABLE IF EXISTS `app_slider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_slider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL,
  `sliderImg` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_slider`
--

LOCK TABLES `app_slider` WRITE;
/*!40000 ALTER TABLE `app_slider` DISABLE KEYS */;
INSERT INTO `app_slider` VALUES (7,'鸭川','upload/鸭川_副本.jpg'),(8,'印度','upload/印度.jpg'),(9,'河西走廊','upload/河西走廊_副本.jpg'),(10,'英伦','upload/英伦_副本.jpg'),(11,'香港','upload/香港.jpg'),(12,'粗乃玩','upload/NeoImage_副本.jpg');
/*!40000 ALTER TABLE `app_slider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_strategy`
--

DROP TABLE IF EXISTS `app_strategy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_strategy` (
  `postable_ptr_id` int(11) NOT NULL,
  `scenerys_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`postable_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_strategy`
--

LOCK TABLES `app_strategy` WRITE;
/*!40000 ALTER TABLE `app_strategy` DISABLE KEYS */;
INSERT INTO `app_strategy` VALUES (4,5),(5,15),(6,13),(7,18);
/*!40000 ALTER TABLE `app_strategy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_strategyscenery`
--

DROP TABLE IF EXISTS `app_strategyscenery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_strategyscenery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `strategy_id` int(11) NOT NULL,
  `scenery_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_strategyscenery`
--

LOCK TABLES `app_strategyscenery` WRITE;
/*!40000 ALTER TABLE `app_strategyscenery` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_strategyscenery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add scenery',7,'add_scenery'),(20,'Can change scenery',7,'change_scenery'),(21,'Can delete scenery',7,'delete_scenery'),(22,'Can add activity',8,'add_activity'),(23,'Can change activity',8,'change_activity'),(24,'Can delete activity',8,'delete_activity'),(25,'Can add activity scenery',9,'add_activityscenery'),(26,'Can change activity scenery',9,'change_activityscenery'),(27,'Can delete activity scenery',9,'delete_activityscenery'),(28,'Can add person',10,'add_person'),(29,'Can change person',10,'change_person'),(30,'Can delete person',10,'delete_person'),(31,'Can add person activity',11,'add_personactivity'),(32,'Can change person activity',11,'change_personactivity'),(33,'Can delete person activity',11,'delete_personactivity'),(34,'Can add person scenery',12,'add_personscenery'),(35,'Can change person scenery',12,'change_personscenery'),(36,'Can delete person scenery',12,'delete_personscenery'),(37,'Can add postable',13,'add_postable'),(38,'Can change postable',13,'change_postable'),(39,'Can delete postable',13,'delete_postable'),(40,'Can add strategy',14,'add_strategy'),(41,'Can change strategy',14,'change_strategy'),(42,'Can delete strategy',14,'delete_strategy'),(43,'Can add strategy scenery',15,'add_strategyscenery'),(44,'Can change strategy scenery',15,'change_strategyscenery'),(45,'Can delete strategy scenery',15,'delete_strategyscenery'),(46,'Can add slider',16,'add_slider'),(47,'Can change slider',16,'change_slider'),(48,'Can delete slider',16,'delete_slider');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$8NjGHV0lfX8S$G/W+6l/tYxw8l0Uam2e2rwthNpvU2+V6x6PhiBRqaWs=','2015-12-21 04:47:49',1,'rccoder','','','rccoder.net@fmail.com',1,1,'2015-12-21 04:42:34'),(3,'pbkdf2_sha256$20000$IDFm3tyoZBYG$KZMm14uAa0+77MmKza2c8bVA42DUVAS0YAi8Eqj1kgI=','2015-12-25 04:35:12',0,'1111','','','1@q.com',0,1,'2015-12-21 04:48:01'),(4,'pbkdf2_sha256$20000$I2hoIMgJGraG$F/mBaG3N8BNyc8yJvt7jDgh+dwu8oheCCWWVfzWV1hI=',NULL,0,'2222','','','22@qq.com',0,1,'2015-12-22 10:39:31'),(5,'pbkdf2_sha256$20000$9Sj9S5NDAJoZ$+uMckevTfSKFgJ2wzG0LGL2YJvU81LeIlW8MLC9pd5M=',NULL,0,'4444','','','44@qq.com',0,1,'2015-12-22 10:56:17'),(6,'pbkdf2_sha256$20000$ueFSmJeUtuga$EL/s90fWqmPv0F0TVkhXOw86LnH6DjlKvt+yyFejsmQ=','2015-12-22 10:57:14',0,'5555','','','55@qq.com',0,1,'2015-12-22 10:56:50'),(7,'pbkdf2_sha256$20000$EScd2RTPKHV7$Mpnd7TgYj1vpbrd/752vULQXYkR7XKf+dwTOCVq7vSE=','2015-12-25 03:24:39',0,'麦秆吸管','','','straki@163.com',0,1,'2015-12-24 15:14:54'),(8,'pbkdf2_sha256$20000$jcqRUctvtuYP$E6/iterydy9srWI6fceflTaEZ1OpK7nQhGSMRrL/kg8=','2015-12-25 03:25:05',0,'1234','','','1234@qq.com',0,1,'2015-12-25 03:07:51'),(9,'pbkdf2_sha256$20000$RaYBmITKcqke$vxBs3s8VWpLCUPQbfH1DCi3RxOYQZPBhXgCIhm5tw04=','2015-12-25 04:14:01',0,'gggg','','','gggg@qq.com',0,1,'2015-12-25 04:13:53');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'app','activity'),(9,'app','activityscenery'),(10,'app','person'),(11,'app','personactivity'),(12,'app','personscenery'),(13,'app','postable'),(7,'app','scenery'),(16,'app','slider'),(14,'app','strategy'),(15,'app','strategyscenery'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-12-21 04:41:56'),(2,'auth','0001_initial','2015-12-21 04:41:58'),(3,'admin','0001_initial','2015-12-21 04:41:59'),(4,'contenttypes','0002_remove_content_type_name','2015-12-21 04:41:59'),(5,'auth','0002_alter_permission_name_max_length','2015-12-21 04:42:00'),(6,'auth','0003_alter_user_email_max_length','2015-12-21 04:42:00'),(7,'auth','0004_alter_user_username_opts','2015-12-21 04:42:00'),(8,'auth','0005_alter_user_last_login_null','2015-12-21 04:42:00'),(9,'auth','0006_require_contenttypes_0002','2015-12-21 04:42:00'),(10,'sessions','0001_initial','2015-12-21 04:42:01');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4qp1iop284drz7hfv5nn06ho3ez34aog','ZmMwYWI0MDBmNWJkNTU0MTAxNzM2YTk3ZmVmYTliNzhkN2YwNmYzZDp7InVzZXJuYW1lIjoiMTIzNCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJkMTFhZjEwMjM5MTRhMTY1NGQ3ZWYxNjhmYjRiZjQ0Yjk0ZjU5NTIiLCJpc3Jvb3QiOiJOIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiOCJ9','2016-01-08 03:25:05'),('ln45ke0dne7ghaztwzomjgds932scpbt','NGMyOGM1ZjFiY2FjMWQ5YmQ5ZmRjMjY5YTQ4MWNkNjc5ZjNmMWY0YTp7InVzZXJuYW1lIjoiMTExMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjIyNTU5ZGQ0NzgzMDg1ZWQ5NzBhNDlmNDVkM2JmZjVkZTYxZTJlZSIsIl9hdXRoX3VzZXJfaWQiOiIzIiwiaXNyb290IjoiWSJ9','2016-01-08 04:35:12'),('oudqj33plnf5v7i7wsdpzc3eo9f9pt7p','ZTliNjhjNWIyYjM5YmJlMmFiMjJkNWNmYTFkN2QyZjQyNmFhMTZiZjp7InVzZXJuYW1lIjoiMTExMSIsIl9hdXRoX3VzZXJfaGFzaCI6IjYyMjU1OWRkNDc4MzA4NWVkOTcwYTQ5ZjQ1ZDNiZmY1ZGU2MWUyZWUiLCJpc3Jvb3QiOiJZIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMyJ9','2016-01-07 14:54:11'),('qio4biumtmjtfwwql33trqg9pm4x0iiu','NGMyOGM1ZjFiY2FjMWQ5YmQ5ZmRjMjY5YTQ4MWNkNjc5ZjNmMWY0YTp7InVzZXJuYW1lIjoiMTExMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjIyNTU5ZGQ0NzgzMDg1ZWQ5NzBhNDlmNDVkM2JmZjVkZTYxZTJlZSIsIl9hdXRoX3VzZXJfaWQiOiIzIiwiaXNyb290IjoiWSJ9','2016-01-05 12:04:35'),('rgfuijw67mttidbq0nwy45f7gh9i3egi','ZGM2ZGY4M2VhZmU4MmRmNWU0MzllZmUyNTIwNTNkZTUzOGExODlhODp7InVzZXJuYW1lIjoiIiwiaXNyb290IjoiTiJ9','2016-01-08 03:24:39');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-25 13:09:55
