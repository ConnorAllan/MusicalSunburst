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
        for row in reader:
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
        for row in reader:
            #If year is unknown then set year to 0
            try:
                yr = int(row[5])
            except:
                yr = 0
            
            #If we can't find the artist then set it to unknown
            try:
                fnArtist = Artists.objects.filter(pmkArtist=row[2])[0]
            except:
                fnArtist = Artists.objects.filter(pmkArtist='0')[0]
                
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
        for row in reader:
            #drop the row if it has no primary key
            try:
                pmk = int(row[1])
            except:
                continue
            
            #If we can't find the artist then set it to unknown
            if Artists.objects.filter(pmkArtist=row[2]).count():
                fnArtist = Artists.objects.filter(pmkArtist=row[2])[0]
            else:
                fnArtist = Artists.objects.filter(pmkArtist='0')[0]
                
            #See if we can find the associated song, drop row if not found since this is a song DB
            if Songs.objects.filter(pmkSong=row[4]).count():
                fnSong = Songs.objects.filter(pmkSong=row[4])[0]
            else:
                continue
            
            Releases.objects.get_or_create(pmkRelease = pmk,
                                          fldName = row[2],
                                          fnkArtist = fnArtist,
                                          fnkSong = fnSong)
            print(dots[i%4], end='')
            sys.stdout.flush()
            i += 1