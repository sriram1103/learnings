 m = re.match("^(.+):\s+(.*)$", line.strip())
 m = re.match("^([^:]+):\s+.*UUID=\"([^\"]+)\"\s+TYPE=\"([^\"]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m2 = re.match("UUID=([^\s]+)", theDevice)
 m = re.match("^\s*([^\s\d]+)", line)
 m = re.match("^\s*([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m = re.match("^\s*([^\s]+)\s+([^\s]+)", line)
 theFilesToIgnore.append(file)
 elif re.match(r'^\d*$',theNoOfDaysRetain):
 value = re.findall(r'\d+', str(cacheValue))
 level=logging.DEBUG)
 shutil.copy( "/tmp/restore.log", LOGPATH+"/"+"cfrestore_"+time.strftime("%Y%m%d_%H%M%S")+".log")
 sys.exit("Error during restore. Reason: %s" %(e))
 m = re.match("^([^\s]+)\s+([^\s]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)", line)
 if re.match(".*part\d+$", link):
 if re.match(".*sr\d+$", path):
 line = re.sub("^(UUID=)([^\s]+)", self.replaceUUID, line);
