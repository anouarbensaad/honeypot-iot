
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE `log` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `iphacker` varchar(20) NOT NULL,
  `uri` int(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


