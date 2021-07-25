-- MariaDB dump 10.19  Distrib 10.6.3-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: calories
-- ------------------------------------------------------
-- Server version	10.6.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `calorielog`
--

DROP TABLE IF EXISTS `calorielog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calorielog` (
  `food` varchar(255) DEFAULT NULL,
  `servingsize` varchar(255) DEFAULT NULL,
  `servinggrams` int(11) DEFAULT NULL,
  `caloriesperserving` int(11) DEFAULT NULL,
  `myserving` int(11) DEFAULT NULL,
  `mycalories` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calorielog`
--

LOCK TABLES `calorielog` WRITE;
/*!40000 ALTER TABLE `calorielog` DISABLE KEYS */;
INSERT INTO `calorielog` VALUES ('1 Medium muffin','1',1,340,0,0),('Adobo','1 cup',241,454,0,0),('Anko dango','3 balls with anko',1,161,0,0),('Avocado','100g',100,160,0,0),('Baguette','50g',50,130,0,0),('Baked beans','100g',100,155,0,0),('Baked ziti','100g',100,156,0,0),('Banana','1 medium',1,105,0,0),('Banana bread','100g',100,326,0,0),('Banana bread','100g',100,323,0,0),('Banana chips','30g',30,150,0,0),('Beef masala curry','200g',200,277,0,0),('Beef Tapa','80g',80,164,0,0),('Beef udon','1 bowl/3 cups',837,638,0,0),('Bibimbap','1 bowl',864,972,0,0),('Bicol express','1 cup',263,605,0,0),('Black beans and rice','100g',100,151,0,0),('Blue cheese dressing','1 tbsp',1,73,0,0),('Blueberry cheesecake','222g',222,495,0,0),('Blueberry jam (hero)','1 tbsp',20,50,0,0),('Bok choy (Stir fried)','369g',369,84,0,0),('Bread','2 slices',1,153,0,0),('Bread pudding','1 cup',200,377,0,0),('Bread sticks','100g',100,412,0,0),('Brioche','85g',85,292,0,0),('Brussel sprouts (roasted)','1 cup',162,135,0,0),('Buffalo wings','1 wing',37,70,0,0),('Burrito (no cheese)','1',1,350,0,0),('Butter','1 tbsp',15,110,0,0),('Cabbage and sausage','1 oz',28,25,0,0),('Caldereta (Purefoods)','112g',112,319,0,0),('Caramel ice cream','100g',100,214,0,0),('Carbonara','1 cup',169,336,0,0),('Carrot fried','227g',227,133,0,0),('Cashews roasted','1 cashew',2,9,0,0),('Chapatha','100g',100,297,0,0),('Cheesecake','100g',100,321,0,0),('Chia seeds','100g',100,486,0,0),('Chicken adobo','1 cup',221,392,0,0),('Chicken biryani','300g',300,417,0,0),('Chicken curry','1 bowl',1,242,0,0),('Chicken korma curry','100g',100,166,0,0),('Chicken noodle soup','100g',100,41,0,0),('Chicken nugget','100g',100,296,0,0),('Chicken ramen (nissin)','1 pack?',1,380,0,0),('Chinese fried rice','100g',100,163,0,0),('Chocolate chip banana bread','90g',90,279,0,0),('Chocolate chip cookie','100g',100,488,0,0),('Ciabatta','2 oz',57,131,0,0),('Cinnamon roll (starbucks)','1 roll',118,420,0,0),('Coconut chicken (tinutungan?)','1 cup',135,280,0,0),('Coconut pork curry','100g',100,420,0,0),('Coffee cake','100g',100,331,0,0),('Cold Brew Coffee (1-1)','\"1 mug ish (1/2 mug of cold brew',1,1,35,0),('Corned tuna','93g times 2 in 1 can',93,56,0,0),('Crackers','100g',100,421,0,0),('Curry pasta','126g',126,165,0,0),('Curry udon','1 cup',473,492,0,0),('Donut (plain)','1',1,200,0,0),('Duck congee/porridge','573',573,596,0,0),('Dumpling','100g',100,112,0,0),('Eden cheese','30g',30,90,0,0),('Egg (boiled)','1',1,70,0,0),('Egg (scrambled)','1 piece',1,91,0,0),('Filipino fruit salad','202g',202,211,0,0),('Fish and tofu (Chinese)','200g',200,327,0,0),('Fish cake (korean)','120g',120,175,0,0),('Flatbread (cheese and tomato)','54g',54,145,0,0),('Foccacia','100g',100,250,0,0),('French fries (baked)','1 cup',58,83,0,0),('Froot Loops','1 cup (29g)',29,110,0,0),('Frosted Flakes','100g',100,369,0,0),('Fruity Pebbles','100g',100,400,0,0),('Garlic fried rice','100g',100,168,0,0),('Ginataang Sitaw Kalabasa','1 cup',180,398,0,0),('Gising-gising','174g',174,159,0,0),('Gouda','1 slice',1,68,0,0),('Grape jam (concord smuckers)','1 tbsp',1,50,0,0),('Green beans fried','100g',100,178,0,0),('Grilled cheese sandwich','1 sandwich',1,440,0,0),('Ground pork fried','100g',100,297,0,0),('Ham (Lotte korean) ','30g',30,65,0,0),('Hash brown','1 pattie',1,130,0,0),('Hazelnut latte (Nescafe)','1',1,74,0,0),('Honey','1 tsp',7,21,0,0),('Honey mustard dip','1 tbsp',1,69,0,0),('Hong Kong fried noodles','292g',292,466,0,0),('Hot chocolate','1 cup',1,120,0,0),('Indomie mi goreng','1 pack',1,410,0,0),('Kimchi','1 cup',150,23,0,0),('Kimchi fried rice','200g',200,149,0,0),('Kouign Amann','93.5g',94,339,0,0),('Krispy Kreme glazed donut','1 donut',1,190,0,0),('Laing','1 cup',75,240,0,0),('Lemon cookie','\"1 2\"\" cookie\"',23,91,0,0),('Lemon salmon','125g (1 pack)',125,289,0,0),('Liege waffle','99g',99,420,0,0),('Lowfat milk (Emborg)','100 ml',100,47,0,0),('Mac and cheese calories','100g',100,164,0,0),('Machang','100g',100,190,0,0),('Maki','1 roll',1,300,0,0),('Mango','100g ',100,60,0,0),('Mapo tofu','2 cups',471,482,0,0),('Mapo tofu (vegetarian)','2 cups',412,377,0,0),('Margherita pizza','\"1 14\"\" slice (107g)\"',107,285,0,0),('Mashed potatoes','100g',100,88,15,0),('Mayonnaise','1 tbsp',14,94,0,0),('Mayver\'s super spread','1 tbsp',20,128,0,0),('Meatloaf','100g',100,149,0,0),('Milk (powdered)','1 tsp',1,17,0,0),('Miso','100g',100,176,0,0),('Mixed veg (sauteed)','1 cup',140,45,0,0),('Mochi (store)','1 pc',1,90,0,0),('Moong dal curry','1 cup (206g)',206,236,0,0),('Oatmeal (cooked)','1 cup (234g)',234,158,0,0),('Olive oil extra virgin','1 tbsp',1,120,0,0),('Palak paneer','1 cup',168,325,0,0),('Pancakes','100g',100,227,0,0),('Pancit canton (cooked)','1 cup',209,207,0,0),('Pancit canton calamnasi (lucky me)','1',1,351,0,0),('Parmesan','1 tbsp',5,20,0,0),('Pasta salad','1 cup',204,414,0,0),('Peanut butter (generic)','1 tablespoon (20g)',20,95,0,0),('Peanut butter (lily\'s)','1 tablespoon (20g)',20,120,0,0),('Peas (fried)','1 cup',182,237,0,0),('Peas and rice','100g',100,145,0,0),('Pechay','100g',100,10,0,0),('Pesto pasta','1 cu',169,367,0,0),('Pizza','1 slice',107,285,0,0),('Popcorn homemade without butter','1 cup',9,35,0,0),('Pork giniling','1 cup',201,246,0,0),('Pork udon','1 bowl',460,428,0,0),('Pork sauteed','3 oz',84,178,0,0),('Potato chips baked','28g',28,120,0,0),('Potato salad with egg','100g',100,157,0,0),('Protein smoothie','1',1,138,0,0),('Puto','1 oz',28,77,0,0),('Quiche (crustless)','100g',100,231,0,0),('Raisins','1 oz/50 raisins (26g)',26,78,0,0),('Refried beans','1 tbsp',1,30,0,0),('Revel bar','57g',57,239,0,0),('Rice','1 cup (158g)',158,206,0,0),('Roast chicken','100g',100,239,0,0),('Roast chickpeas','100g',100,364,0,0),('Roti','100g',100,297,0,0),('Saba (boiled)','2 pieces',2,220,0,0),('Sardine pasta','1 cup',200,343,0,0),('Sardines (spanish D Elena)','2 oz',57,170,0,0),('Sardines (spanish pandemnl)','4',55,250,0,0),('Sauerkraut','100g',100,19,0,0),('Sauteed broccoli','1 cup',156,70,0,0),('Sauteed chicken','100g',100,223,0,0),('Scone','115g',115,398,0,0),('Seafood pancake','1',314,464,0,0),('Sesame oil','1 tsp',1,40,0,0),('Shrimp','1 piece',1,7,0,0),('Shrimp roll (egg roll type)','1 piece',130,164,0,0),('Shumai','1 pc',27,59,0,0),('Siopao / pork bao','93g',93,217,0,0),('Snickerdoodle','1 piece',1,90,0,0),('Soy chicken','214g',214,382,0,0),('spaghetti (plain noodles)','1 cup',140,221,0,0),('Spaghetti bolognese','2 cups (330g)',330,334,0,0),('Spaghetti pomodoro','1 cup',248,318,0,0),('Spaghetti sauce (Filipino style pack)','125g (1 pack)',125,70,0,0),('Squash soup','2 cups',490,220,0,0),('Steak','100g',100,271,0,0),('Steamed rice roll','136g',136,161,0,0),('Strawberry jam (cheap)','100g',100,278,0,0),('Sugar','1 tsp',1,15,0,0),('Suman','1 piece',1,63,0,0),('Sweet and sour pork','100g',100,270,0,0),('Sweet potato chips (kamote chips)','28g',28,148,0,0),('Taco (soft chicken no cheese)','1',1,130,0,0),('Tamago','76g',76,103,0,0),('Thit kho','4 oz',112,227,0,0),('Tofu sauteed','1 cup',217,162,0,0),('Tomato','100g',100,18,0,0),('Tomato sauce','100g',100,29,0,0),('Tomato sauteed','0.5 cup',149,27,0,0),('Tonkatsu','199g',199,498,0,0),('Tonkatsu sauce','1 tbsp',1,20,0,0),('Trail Mix','100g',100,462,0,0),('Tuna','56g (3 per can)',56,100,0,0),('Tuna curry','56g (3 per can)',56,84,0,0),('Tuna salad','\"2 small cans',2,1,788,0),('Tupig','13 pcs',13,686,0,0),('Various dimsum','52g',52,120,0,0),('Veega meatballs','4 pieces',4,140,0,0),('Vermicceli soup','170g',170,120,0,0),('Vienna sausage','1 pc',1,37,0,0),('White beans boiled','100g',100,140,0,0),('White bread','100g',100,265,0,0),('White cheddar','100g',100,409,0,0),('Whole wheat bread gardenia','2 slices',2,170,0,0),('Whole wheat roll',' 36g',36,96,0,0),('Yema spread','15g',15,50,0,0),('Zenzai','1 cup',151,336,0,0);
/*!40000 ALTER TABLE `calorielog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diary`
--

DROP TABLE IF EXISTS `diary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diary` (
  `date` date DEFAULT NULL,
  `weight` decimal(10,0) DEFAULT NULL,
  `exercised` tinyint(1) DEFAULT NULL,
  `overate` tinyint(1) DEFAULT NULL,
  `breakfast` varchar(255) DEFAULT NULL,
  `bcalories` int(11) DEFAULT NULL,
  `lunch` varchar(255) DEFAULT NULL,
  `lcalories` int(11) DEFAULT NULL,
  `dinner` varchar(255) DEFAULT NULL,
  `dcalories` int(11) DEFAULT NULL,
  `snack1` varchar(255) DEFAULT NULL,
  `s1calories` int(11) DEFAULT NULL,
  `snack2` varchar(255) DEFAULT NULL,
  `s2calories` int(11) DEFAULT NULL,
  `snack3` varchar(255) DEFAULT NULL,
  `s3calories` int(11) DEFAULT NULL,
  `snack4` varchar(255) DEFAULT NULL,
  `s4calories` int(11) DEFAULT NULL,
  `snack5` varchar(255) DEFAULT NULL,
  `s5calories` int(11) DEFAULT NULL,
  `snack6` varchar(255) DEFAULT NULL,
  `s6calories` int(11) DEFAULT NULL,
  `totalcalories` int(11) DEFAULT NULL,
  `maxcalories` int(11) DEFAULT NULL,
  `caloriesleft` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diary`
--

LOCK TABLES `diary` WRITE;
/*!40000 ALTER TABLE `diary` DISABLE KEYS */;
/*!40000 ALTER TABLE `diary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-25 15:48:49
