CREATE SCHEMA db;
use db;
CREATE TABLE `props` (
  `pid` varchar(20) NOT NULL,
  `p_price` varchar(30) DEFAULT NULL,
  `p_category` varchar(30) DEFAULT NULL,
  `p_status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`pid`)
);
CREATE TABLE `footwear` (
  `fid` varchar(20) NOT NULL,
  `f_price` varchar(30) DEFAULT NULL,
  `f_category` varchar(30) DEFAULT NULL,
  `f_status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`fid`)
);
 CREATE TABLE `jewellery` (
  `jid` varchar(20) NOT NULL,
  `j_price` varchar(30) DEFAULT NULL,
  `j_category` varchar(30) DEFAULT NULL,
  `j_status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`jid`)
);
CREATE TABLE `costumes` (
  `cid` varchar(20) NOT NULL,
  `item_name` varchar(30) DEFAULT NULL,
  `c_category` varchar(30) DEFAULT NULL,
  `c_status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cid`)
  );
CREATE TABLE `costumes_backup` (
  `cid` varchar(20) NOT NULL,
  `item_name` varchar(30) DEFAULT NULL,
  `c_category` varchar(30) DEFAULT NULL,
  `c_status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cid`)
  );
 CREATE TABLE `items_issued` (
  `cid` varchar(20) DEFAULT NULL,
  `jid` varchar(20) DEFAULT NULL,
  `pid` varchar(20) DEFAULT NULL,
  `fid` varchar(20) DEFAULT NULL,
  `issuedto` varchar(30) DEFAULT NULL,
  `contact_number` varchar(10) DEFAULT NULL
);
  
ALTER TABLE `items_issued`
ADD CONSTRAINT `FK_cid_costumes`
FOREIGN KEY (cid)
REFERENCES costumes(cid);

ALTER TABLE `items_issued`
ADD CONSTRAINT `FK_jid_jobs`
FOREIGN KEY (`jid`)
REFERENCES `jewellery` (`jid`);

ALTER TABLE `items_issued`
ADD CONSTRAINT `FK_pid_projects`
FOREIGN KEY (`pid`)
REFERENCES `props` (`pid`);

ALTER TABLE `items_issued`
ADD CONSTRAINT `FK_fid_festivals`
FOREIGN KEY (`fid`)
REFERENCES `footwear` (`fid`);
  
  
DELIMITER //
CREATE TRIGGER backup_deleted_costumes
AFTER DELETE ON costumes
FOR EACH ROW
BEGIN
    INSERT INTO costumes_backup (cid, item_name, c_category, c_status)
    VALUES (OLD.cid, OLD.item_name, OLD.c_category, OLD.c_status);
END;
//
DELIMITER ;



DELIMITER //

CREATE PROCEDURE ValidatePhoneNumber(IN phone_number VARCHAR(15), OUT validation_result VARCHAR(50))
BEGIN
    DECLARE first_digit CHAR(1);

    SET first_digit = LEFT(phone_number, 1);

    IF LENGTH(phone_number) = 10 AND first_digit IN ('6', '7', '8', '9') THEN
        SET validation_result = 'Phone number is valid';
    ELSE
        SET validation_result = 'Invalid phone number';
    END IF;
END;

//
DELIMITER ;

SET @result = '';

CALL ValidatePhoneNumber(contact_number, @result);
SELECT @result AS 'Validation Result';
