-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: searchengine
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `ignoredword`
--

DROP TABLE IF EXISTS `ignoredword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ignoredword` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ignoredWord` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ignoredWord_UNIQUE` (`ignoredWord`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ignoredword`
--

LOCK TABLES `ignoredword` WRITE;
/*!40000 ALTER TABLE `ignoredword` DISABLE KEYS */;
INSERT INTO `ignoredword` VALUES (35,'\''),(34,','),(36,'-'),(37,'/'),(33,':'),(17,'a'),(66,'after'),(3,'am'),(18,'an'),(55,'and'),(2,'are'),(58,'be'),(59,'been'),(67,'befor'),(73,'but'),(27,'can'),(28,'could'),(61,'did'),(60,'do'),(62,'does'),(64,'for'),(65,'from'),(4,'has'),(5,'have'),(9,'he'),(70,'here'),(69,'him'),(68,'his'),(75,'however'),(11,'i'),(30,'in'),(57,'into'),(1,'is'),(10,'it'),(77,'may'),(78,'might'),(71,'not'),(63,'of'),(31,'on'),(25,'shall'),(8,'she'),(26,'should'),(21,'that'),(19,'the'),(15,'their'),(13,'them'),(14,'there'),(12,'they'),(20,'this'),(22,'those'),(56,'to'),(72,'too'),(16,'us'),(6,'was'),(7,'were'),(23,'will'),(32,'with'),(24,'would'),(79,'you'),(76,'your');
/*!40000 ALTER TABLE `ignoredword` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-14  7:00:29
