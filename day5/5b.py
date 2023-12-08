file = open('5.txt', 'r')
fileText = file.read()

def parseMap(mapType):
	finalMap = {}
	text = fileText.split(mapType)[1].split("\n\n")[0]
	mapArray = text.split("\n")
	for mapLine in mapArray:
		mapLineArray = mapLine.split(" ")
		finalMap[range(int(mapLineArray[0]), int(mapLineArray[0]) + int(mapLineArray[2]))] = int(mapLineArray[1])
	return finalMap

def findSeed(loc):
	hum = getMappedVal(loc, locToHum)
	temp = getMappedVal(hum, humToTemp)
	light = getMappedVal(temp, tempToLight)
	water = getMappedVal(light, lightToWater)
	fert = getMappedVal(water, waterToFert)
	soil = getMappedVal(fert, fertToSoil)
	seed = getMappedVal(soil, soilToSeed)
	return seed

def getSeeds():
	nums = fileText.split("seeds:")[1].split("\n\n")[0].strip().split(" ")
	# split into pairs of numbers
	both = False
	seeds = []

	for i in range(0, len(nums), 2):
		seeds.append(range(int(nums[i]), int(nums[i]) + int(nums[i+1])))
	return seeds

def getMappedVal(val, map):
	for key in map.keys():
		if val in key:
			return map[key] - key[0] + val
	return val


seeds = getSeeds()

soilToSeed = parseMap("seed-to-soil map:\n")
fertToSoil = parseMap("soil-to-fertilizer map:\n")
waterToFert = parseMap("fertilizer-to-water map:\n")
lightToWater = parseMap("water-to-light map:\n")
tempToLight = parseMap("light-to-temperature map:\n")
humToTemp = parseMap("temperature-to-humidity map:\n")
locToHum = parseMap("humidity-to-location map:\n")

def f():
	for loc in range(0, 10000000000):
		print("trying loc: ", loc)
		seed = findSeed(loc)
		for seedRange in seeds:
			if seed in seedRange:
				# found!
				print("found", loc)
				return
f()



