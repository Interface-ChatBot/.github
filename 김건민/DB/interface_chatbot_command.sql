-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: interface_chatbot
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `command`
--

DROP TABLE IF EXISTS `command`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `command` (
  `command` varchar(100) DEFAULT NULL,
  `example` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `command`
--

LOCK TABLES `command` WRITE;
/*!40000 ALTER TABLE `command` DISABLE KEYS */;
INSERT INTO `command` VALUES ('wifi','와이파이'),('wifi','와이파이 비밀번호'),('wifi','wifi 비밀번호'),('wifi','wifi 비번'),('wifi','wifi'),('wifi','와이파이 비번'),('동아리 소개','동아리 소개'),('동아리 소개','인터페이스 소개'),('동아리 소개','인페 소개'),('동아리 건의사항','건의사항'),('동아리 건의사항','건의'),('동아리 건의사항','동아리 건의사항'),('동아리 활동 일정','동아리 활동 일정'),('동아리 활동 일정','활동'),('동아리 활동 일정','일정'),('동아리 활동 일정','동아리 일정'),('동아리 활동 일정','동아리 활동'),('동아리 기수 구분','동아리 기수 구분'),('동아리 기수 구분','동아리 인원수'),('동아리 기수 구분','인원수'),('동아리 기수 구분','인원'),('동아리 기수 구분','동아리 기수'),('동아리 건의사항','필요'),('동아리 건의사항','필요물품'),('집부 구성원','집부 구성원'),('집부 구성원','집부'),('집부 구성원','회장'),('집부 구성원','부회장'),('집부 구성원','기장'),('집부 구성원','총무'),('집부 구성원','집행 부원'),('집부 구성원','집행부'),('동아리 링크','동아리 링크'),('동아리 링크','홈페이지'),('동아리 링크','이메일'),('동아리 링크','깃허브'),('동아리 링크','홈피'),('동아리 링크','인스타그램'),('동아리 링크','페이스북'),('동아리 위치','동아리 위치'),('동아리 위치','동아리 방'),('동아리 위치','동방'),('동아리 위치','동방 위치'),('동아리 위치','동아리 방 위치'),('동아리 회비','동아리 회비'),('동아리 회비','회비'),('동아리 회비','가입비'),('동아리 회비','활동비'),('동아리 회비','동아리비'),('동아리 소개','인페 소개'),('동아리 건의사항','인페 건의사항'),('동아리 건의사항','인터페이스 건의사항'),('동아리 활동 일정','인터페이스 활동 일정'),('동아리 활동 일정','인페 활동 일정'),('동아리 링크','인터페이스 링크'),('동아리 링크','인페 링크'),('동아리 위치','인터페이스 위치'),('동아리 위치','인페 위치'),('동아리 회비','인터페이스 회비'),('동아리 회비','인페 회비');
/*!40000 ALTER TABLE `command` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-28 19:44:05
