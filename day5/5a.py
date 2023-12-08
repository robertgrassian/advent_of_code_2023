file = open('5.txt', 'r')
fileText = file.read()

def parseMap(mapType):
	finalMap = {}
	text = fileText.split(mapType)[1].split("\n\n")[0]
	mapArray = text.split("\n")
	for mapLine in mapArray:
		mapLineArray = mapLine.split(" ")
		finalMap[range(int(mapLineArray[1]), int(mapLineArray[1]) + int(mapLineArray[2]))] = int(mapLineArray[0])
	return finalMap

def findLoc(seed):
		soil = getMappedVal(seed, seedToSoil)
		fert = getMappedVal(soil, soilToFert)
		water = getMappedVal(fert, fertToWater)
		light = getMappedVal(water, waterToLight)
		temp = getMappedVal(light, lightToTemp)
		hum = getMappedVal(temp, tempToHum)
		loc = getMappedVal(hum, humToLoc)
		return loc

def getSeeds():
	# first line
	return fileText.split("seeds:")[1].split("\n\n")[0].strip().split(" ")

def getMappedVal(val, map):
	for key in map.keys():
		if val in key:
			return map[key] - key[0] + val
	return val


seeds = getSeeds()

seedToSoil = parseMap("seed-to-soil map:\n")
soilToFert = parseMap("soil-to-fertilizer map:\n")
fertToWater = parseMap("fertilizer-to-water map:\n")
waterToLight = parseMap("water-to-light map:\n")
lightToTemp = parseMap("light-to-temperature map:\n")
tempToHum = parseMap("temperature-to-humidity map:\n")
humToLoc = parseMap("humidity-to-location map:\n")

a = [findLoc(int(x)) for x in seeds]
print(min(a))

