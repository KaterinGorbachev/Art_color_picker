-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema art_color_picker
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema art_color_picker
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `art_color_picker` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `art_color_picker` ;

-- -----------------------------------------------------
-- Table `art_color_picker`.`colors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art_color_picker`.`colors` ;

CREATE TABLE IF NOT EXISTS `art_color_picker`.`colors` (
  `rgb` INT UNSIGNED NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `cmyk` JSON NULL,
  PRIMARY KEY (`rgb`),
  UNIQUE INDEX `rgb_UNIQUE` (`rgb` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art_color_picker`.`palletes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art_color_picker`.`palletes` ;

CREATE TABLE IF NOT EXISTS `art_color_picker`.`palletes` (
  `number` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`number`),
  UNIQUE INDEX `number_UNIQUE` (`number` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art_color_picker`.`palletes_has_colors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art_color_picker`.`palletes_has_colors` ;

CREATE TABLE IF NOT EXISTS `art_color_picker`.`palletes_has_colors` (
  `palletes_number` INT UNSIGNED NOT NULL,
  `colors_rgb` INT UNSIGNED NOT NULL,
  `position` SMALLINT UNSIGNED NULL,
  INDEX `fk_palletes_has_colors_colors1_idx` (`colors_rgb` ASC) VISIBLE,
  INDEX `fk_palletes_has_colors_palletes_idx` (`palletes_number` ASC) VISIBLE,
  CONSTRAINT `fk_palletes_has_colors_palletes`
    FOREIGN KEY (`palletes_number`)
    REFERENCES `art_color_picker`.`palletes` (`number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_palletes_has_colors_colors1`
    FOREIGN KEY (`colors_rgb`)
    REFERENCES `art_color_picker`.`colors` (`rgb`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art_color_picker`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art_color_picker`.`user` ;

CREATE TABLE IF NOT EXISTS `art_color_picker`.`user` (
  `id_user` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_user`),
  UNIQUE INDEX `id_user_UNIQUE` (`id_user` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art_color_picker`.`collection`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art_color_picker`.`collection` ;

CREATE TABLE IF NOT EXISTS `art_color_picker`.`collection` (
  `palletes_number` INT UNSIGNED NOT NULL,
  `user_id_user` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`palletes_number`, `user_id_user`),
  INDEX `fk_palletes_has_user_user1_idx` (`user_id_user` ASC) VISIBLE,
  INDEX `fk_palletes_has_user_palletes1_idx` (`palletes_number` ASC) VISIBLE,
  CONSTRAINT `fk_palletes_has_user_palletes1`
    FOREIGN KEY (`palletes_number`)
    REFERENCES `art_color_picker`.`palletes` (`number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_palletes_has_user_user1`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `art_color_picker`.`user` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
