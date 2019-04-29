def run():
    from sunburst.models import Artists, Songs, Releases
    import csv, sys
    dataDir = "../extra/"
    
    dots = ['\r   ', '\r.  ', '\r.. ', '\r...']
    i = 0
    
    print("This may take a few minutes")
    print("Loading Artists")
    
    #create a special entry for unknown artist
    Artists.objects.get_or_create(pmkArtist = "0",
                                          fldName = "Unknown",
                                          fldLocation = "Not available")
    with open(dataDir + "Artists.csv") as csvFile:
        reader = csv.reader(csvFile)
        #skip headers
        next(reader)
        for row in reader:
            #make sure the artist isn't already in the system, skips conflictingg entries
            preExisting = Artists.objects.filter(pmkArtist = row[1])
            if preExisting.count():
                continue
            
            #get or create skips duplicate entriees
            Artists.objects.get_or_create(pmkArtist = row[1],
                                          fldName = row[2],
                                          fldLocation = row[3])
            print(dots[i%4], end='')
            sys.stdout.flush()
            i += 1
            
    i = 0
    print("\nLoading Songs")
    with open(dataDir + "Songs.csv") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            
            preExisting = Songs.objects.filter(pmkSong = row[1])
            if preExisting.count():
                continue
            
            #If year is unknown then set year to 0
            try:
                yr = int(row[5])
            except:
                yr = 0
            
            #If we can't find the artist then set it to unknown
            try:
                fnArtist = Artists.objects.get( pmkArtist = row[2] )
            except:
                print("ARTIST UNKNOWN")
                fnArtist = Artists.objects.get( pmkArtist = '0')
                
            Songs.objects.get_or_create(pmkSong = row[1],
                                        fnkArtist = fnArtist,
                                        fldTerms = row[3],
                                        fldTitle = row[4],
                                        fldYear = yr)
            print(dots[i%4], end='')
            sys.stdout.flush()
            i += 1
    i = 0
    print("\nLoading Releases")        
    with open(dataDir + "Releases.csv") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            
            #drop the row if it has no primary key
            try:
                pmk = int(row[1])
            except:
                continue
            
            preExisting = Releases.objects.filter(pmkRelease = row[1])
            if preExisting.count():
                continue
            
            #If we can't find the artist then set it to unknown
            try:
                fnArtist = Artists.objects.get(pmkArtist=row[3])
            except:
                print("ARTIST UNKNOWN")
                fnArtist = Artists.objects.get( pmkArtist = '0')
                
            #See if we can find the associated song, drop row if not found since this is a song DB
            try:
                fnSong = Songs.objects.get(pmkSong=row[4])
            except:
                print("SONG UNKNOWN")
                continue
            
            Releases.objects.get_or_create(pmkRelease = pmk,
                                          fldName = row[2],
                                          fnkArtist = fnArtist,
                                          fnkSong = fnSong)
            print(dots[i%4], end='')
            sys.stdout.flush()
            i += 1