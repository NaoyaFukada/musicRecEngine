from collections import deque

music_graph = {
    # --------------------------------------------------------------------------
    # 1. Core POP Genre Node listing all artists
    # --------------------------------------------------------------------------
    "Pop": [
        "Taylor Swift", "Ed Sheeran", "Ariana Grande", "Dua Lipa", "Justin Bieber",
        "Selena Gomez", "Maroon 5", "Bruno Mars", "Katy Perry", "Rihanna",
        "Jason Derulo", "Shawn Mendes", "Charlie Puth", "Camila Cabello",
        "Lady Gaga", "Adele", "One Direction", "Billie Eilish", "Troye Sivan",
        "Meghan Trainor", "Carly Rae Jepsen"
    ],
    
    # --------------------------------------------------------------------------
    # 2. Artists -> Their Songs + "Pop"
    # --------------------------------------------------------------------------
    "Taylor Swift": [
        "Bad Blood", "Shake It Off", "Blank Space", "Love Story", "You Belong with Me",
        "Delicate", "Style", "22", "I Knew You Were Trouble", "Look What You Made Me Do",
        "Pop"
    ],
    "Ed Sheeran": [
        "Shape of You", "Perfect", "Thinking Out Loud", "Castle on the Hill", "Photograph",
        "Galway Girl", "I Don't Care", "Pop"
    ],
    "Ariana Grande": [
        "7 Rings", "No Tears Left to Cry", "Into You", "Side to Side", "One Last Time",
        "Dangerous Woman", "Focus", "Break Free", "Pop"
    ],
    "Dua Lipa": [
        "Don't Start Now", "New Rules", "Levitating", "Physical", "IDGAF",
        "Be the One", "Hotter Than Hell", "Pop"
    ],
    "Justin Bieber": [
        "Baby", "Love Yourself", "Sorry", "What Do You Mean", "Intentions", "Peaches",
        "Boyfriend", "Beauty and a Beat", "I Don't Care", "Pop"
    ],
    "Selena Gomez": [
        "Hands to Myself", "Come & Get It", "Lose You to Love Me", "Wolves", "Same Old Love",
        "Good for You", "The Heart Wants What It Wants", "Pop"
    ],
    "Maroon 5": [
        "Sugar", "Girls Like You", "Memories", "Moves Like Jagger", "Payphone",
        "She Will Be Loved", "Maps", "Animals", "Pop"
    ],
    "Bruno Mars": [
        "Uptown Funk", "24K Magic", "That's What I Like", "Locked Out of Heaven", "Treasure",
        "Grenade", "Just the Way You Are", "Pop"
    ],
    "Katy Perry": [
        "Roar", "Firework", "Teenage Dream", "Dark Horse", "California Gurls",
        "The One That Got Away", "Last Friday Night (T.G.I.F.)", "Part of Me", "Pop"
    ],
    "Rihanna": [
        "Diamonds", "We Found Love", "Umbrella", "Only Girl (In the World)", "Stay",
        "Work", "Rude Boy", "Pop"
    ],
    "Jason Derulo": [
        "Trumpets", "Want to Want Me", "Talk Dirty", "Wiggle", "Ridin' Solo",
        "Marry Me", "In My Head", "Pop"
    ],
    "Shawn Mendes": [
        "Stitches", "Treat You Better", "There's Nothing Holdin' Me Back", "Senorita",
        "If I Can't Have You", "Mercy", "In My Blood", "Pop"
    ],
    "Charlie Puth": [
        "Attention", "We Don't Talk Anymore", "One Call Away", "How Long",
        "Marvin Gaye", "See You Again", "Pop"
    ],
    "Camila Cabello": [
        "Havana", "Never Be the Same", "Senorita", "Crying in the Club",
        "Liar", "I Have Questions", "Pop"
    ],
    "Lady Gaga": [
        "Shallow", "Bad Romance", "Poker Face", "Born This Way", "Stupid Love",
        "Rain on Me", "The Edge of Glory", "Telephone", "Pop"
    ],
    "Adele": [
        "Rolling in the Deep", "Someone Like You", "Hello", "Set Fire to the Rain",
        "When We Were Young", "Send My Love (To Your New Lover)", "Skyfall", "Pop"
    ],
    "One Direction": [
        "What Makes You Beautiful", "Story of My Life", "Drag Me Down", "Best Song Ever",
        "Little Things", "One Thing", "Pop"
    ],
    "Billie Eilish": [
        "Bad Guy", "Ocean Eyes", "Everything I Wanted", "Bury a Friend",
        "When the Party's Over", "Lovely", "Pop"
    ],
    "Troye Sivan": [
        "Youth", "My My My!", "Wild", "Talk Me Down",
        "Strawberries & Cigarettes", "Bloom", "Pop"
    ],
    "Meghan Trainor": [
        "All About That Bass", "Like I'm Gonna Lose You", "No", "Lips Are Movin",
        "Dear Future Husband", "Me Too", "Pop"
    ],
    "Carly Rae Jepsen": [
        "Call Me Maybe", "I Really Like You", "Run Away with Me", "Good Time",
        "Cut to the Feeling", "Pop"
    ],
    
    # --------------------------------------------------------------------------
    # 3. Song Nodes with ≥5 references each
    #    Format: "Song Title": [Artist, plus ~4 other songs]
    # --------------------------------------------------------------------------
    
    # -------------------- TAYLOR SWIFT --------------------
    "Bad Blood": [
        "Taylor Swift", "7 Rings", "Blank Space", "We Found Love", "Senorita", 
        "Look What You Made Me Do"
    ],
    "Shake It Off": [
        "Taylor Swift", "Pop", "Blank Space", "Uptown Funk", "22"
    ],
    "Blank Space": [
        "Taylor Swift", "Bad Blood", "Shake It Off", "I Knew You Were Trouble", 
        "Look What You Made Me Do"
    ],
    "Love Story": [
        "Taylor Swift", "Thinking Out Loud", "Photograph", "You Belong with Me", 
        "22"
    ],
    "You Belong with Me": [
        "Taylor Swift", "Love Story", "22", "Blank Space", "Style"
    ],
    "Delicate": [
        "Taylor Swift", "Style", "Look What You Made Me Do", "22", "Blank Space"
    ],
    "Style": [
        "Taylor Swift", "Delicate", "Photograph", "Shake It Off", "Blank Space"
    ],
    "22": [
        "Taylor Swift", "Shake It Off", "You Belong with Me", "I Knew You Were Trouble",
        "Look What You Made Me Do"
    ],
    "I Knew You Were Trouble": [
        "Taylor Swift", "22", "Blank Space", "I Don't Care", "Shake It Off"
    ],
    "Look What You Made Me Do": [
        "Taylor Swift", "Bad Blood", "Delicate", "Havana", "Blank Space"
    ],
    
    # -------------------- ED SHEERAN --------------------
    "Shape of You": [
        "Ed Sheeran", "Love Yourself", "Thinking Out Loud", "Photograph", "Perfect"
    ],
    "Perfect": [
        "Ed Sheeran", "Castle on the Hill", "Shape of You", "Thinking Out Loud", 
        "IDGAF"
    ],
    "Thinking Out Loud": [
        "Ed Sheeran", "Love Story", "Shape of You", "Photograph", "22"
    ],
    "Castle on the Hill": [
        "Ed Sheeran", "Perfect", "Thinking Out Loud", "Blank Space", "Galway Girl"
    ],
    "Photograph": [
        "Ed Sheeran", "Shape of You", "Love Story", "Blank Space", "Hotter Than Hell"
    ],
    "Galway Girl": [
        "Ed Sheeran", "Photograph", "Focus", "Shake It Off", "Senorita"
    ],
    "I Don't Care": [
        "Ed Sheeran", "Justin Bieber", "I Knew You Were Trouble", "Boyfriend", 
        "New Rules"
    ],
    
    # -------------------- ARIANA GRANDE --------------------
    "7 Rings": [
        "Ariana Grande", "Bad Blood", "No Tears Left to Cry", "Havana", "Focus"
    ],
    "No Tears Left to Cry": [
        "Ariana Grande", "Into You", "Break Free", "Senorita", "Shape of You"
    ],
    "Into You": [
        "Ariana Grande", "No Tears Left to Cry", "Side to Side", "7 Rings", "Havana"
    ],
    "Side to Side": [
        "Ariana Grande", "Into You", "Dangerous Woman", "Break Free", "Focus"
    ],
    "One Last Time": [
        "Ariana Grande", "Focus", "Into You", "Blank Space", "Photograph"
    ],
    "Dangerous Woman": [
        "Ariana Grande", "Side to Side", "Break Free", "7 Rings", "Shake It Off"
    ],
    "Focus": [
        "Ariana Grande", "Galway Girl", "Break Free", "No Tears Left to Cry", 
        "Senorita"
    ],
    "Break Free": [
        "Ariana Grande", "Focus", "Dangerous Woman", "Blank Space", "Hotter Than Hell"
    ],
    
    # -------------------- DUA LIPA --------------------
    "Don't Start Now": [
        "Dua Lipa", "New Rules", "Levitating", "Physical", "Senorita"
    ],
    "New Rules": [
        "Dua Lipa", "Don't Start Now", "IDGAF", "Hotter Than Hell", "What Do You Mean"
    ],
    "Levitating": [
        "Dua Lipa", "Don't Start Now", "Hotter Than Hell", "Physical", 
        "Moves Like Jagger"
    ],
    "Physical": [
        "Dua Lipa", "Don't Start Now", "Be the One", "Levitating", "Rude Boy"
    ],
    "IDGAF": [
        "Dua Lipa", "New Rules", "Hotter Than Hell", "Shake It Off", "Galway Girl"
    ],
    "Be the One": [
        "Dua Lipa", "Physical", "Hotter Than Hell", "Don't Start Now", "Blank Space"
    ],
    "Hotter Than Hell": [
        "Dua Lipa", "Levitating", "Be the One", "IDGAF", "Delicate"
    ],
    
    # -------------------- JUSTIN BIEBER --------------------
    "Baby": [
        "Justin Bieber", "Sorry", "Pop", "Boyfriend", "Love Yourself"
    ],
    "Love Yourself": [
        "Justin Bieber", "Shape of You", "Sorry", "We Don't Talk Anymore", 
        "Photograph"
    ],
    "Sorry": [
        "Justin Bieber", "Baby", "Love Yourself", "What Do You Mean", "Havana"
    ],
    "What Do You Mean": [
        "Justin Bieber", "Boyfriend", "Sorry", "Shake It Off", "In My Blood"
    ],
    "Intentions": [
        "Justin Bieber", "Peaches", "Sorry", "Marry Me", "Uptown Funk"
    ],
    "Peaches": [
        "Justin Bieber", "Intentions", "Senorita", "New Rules", "Castle on the Hill"
    ],
    "Boyfriend": [
        "Justin Bieber", "What Do You Mean", "I Don't Care", "Sorry", "Focus"
    ],
    "Beauty and a Beat": [
        "Justin Bieber", "Baby", "Moves Like Jagger", "Shake It Off", "Bad Blood"
    ],
    
    # -------------------- SELENA GOMEZ --------------------
    "Hands to Myself": [
        "Selena Gomez", "Pop", "Same Old Love", "Focus", "Shallow"
    ],
    "Come & Get It": [
        "Selena Gomez", "Same Old Love", "Rude Boy", "I Knew You Were Trouble",
        "Love Story"
    ],
    "Lose You to Love Me": [
        "Selena Gomez", "Wolves", "One Last Time", "All About That Bass", 
        "Just the Way You Are"
    ],
    "Wolves": [
        "Selena Gomez", "Lose You to Love Me", "Photograph", "Castle on the Hill",
        "Focus"
    ],
    "Same Old Love": [
        "Selena Gomez", "Come & Get It", "Good for You", "Shake It Off", 
        "Look What You Made Me Do"
    ],
    "Good for You": [
        "Selena Gomez", "The Heart Wants What It Wants", "Same Old Love", 
        "Hands to Myself", "Delicate"
    ],
    "The Heart Wants What It Wants": [
        "Selena Gomez", "Good for You", "Blank Space", "Shake It Off", "Stitches"
    ],
    
    # -------------------- MAROON 5 --------------------
    "Sugar": [
        "Maroon 5", "Girls Like You", "Animals", "Dark Horse", "Baby"
    ],
    "Girls Like You": [
        "Maroon 5", "Sugar", "Moves Like Jagger", "Animals", "Shake It Off"
    ],
    "Memories": [
        "Maroon 5", "Animals", "Sugar", "Shallow", "Peaches"
    ],
    "Moves Like Jagger": [
        "Maroon 5", "Girls Like You", "Beauty and a Beat", "Roar", "Levitating"
    ],
    "Payphone": [
        "Maroon 5", "Maps", "Animals", "Sugar", "Don't Start Now"
    ],
    "She Will Be Loved": [
        "Maroon 5", "Sugar", "We Don't Talk Anymore", "Hello", "Teenage Dream"
    ],
    "Maps": [
        "Maroon 5", "Payphone", "Animals", "Girls Like You", "I Don't Care"
    ],
    "Animals": [
        "Maroon 5", "Memories", "Payphone", "Maps", "I Knew You Were Trouble"
    ],
    
    # -------------------- BRUNO MARS --------------------
    "Uptown Funk": [
        "Bruno Mars", "24K Magic", "That's What I Like", "Shake It Off", "Senorita"
    ],
    "24K Magic": [
        "Bruno Mars", "Uptown Funk", "Treasure", "Levitating", "Senorita"
    ],
    "That's What I Like": [
        "Bruno Mars", "Uptown Funk", "Treasure", "24K Magic", "Sugar"
    ],
    "Locked Out of Heaven": [
        "Bruno Mars", "Treasure", "Grenade", "Moves Like Jagger", "Don't Start Now"
    ],
    "Treasure": [
        "Bruno Mars", "Locked Out of Heaven", "That's What I Like", "24K Magic",
        "Uptown Funk"
    ],
    "Grenade": [
        "Bruno Mars", "Locked Out of Heaven", "Just the Way You Are", "Sugar",
        "Senorita"
    ],
    "Just the Way You Are": [
        "Bruno Mars", "Grenade", "Baby", "Lose You to Love Me", "We Found Love"
    ],
    
    # -------------------- KATY PERRY --------------------
    "Roar": [
        "Katy Perry", "Firework", "Teenage Dream", "Moves Like Jagger", "Bad Blood"
    ],
    "Firework": [
        "Katy Perry", "Roar", "Dark Horse", "We Found Love", "Photograph"
    ],
    "Teenage Dream": [
        "Katy Perry", "Roar", "Dark Horse", "Last Friday Night (T.G.I.F.)", "Sugar"
    ],
    "Dark Horse": [
        "Katy Perry", "Teenage Dream", "California Gurls", "Sugar", "Senorita"
    ],
    "California Gurls": [
        "Katy Perry", "Dark Horse", "Last Friday Night (T.G.I.F.)", "New Rules", 
        "Grenade"
    ],
    "The One That Got Away": [
        "Katy Perry", "Teenage Dream", "Blank Space", "Sorry", "She Will Be Loved"
    ],
    "Last Friday Night (T.G.I.F.)": [
        "Katy Perry", "Teenage Dream", "California Gurls", "Focus", "Peaches"
    ],
    "Part of Me": [
        "Katy Perry", "Teenage Dream", "Bad Blood", "Levitating", "We Found Love"
    ],
    
    # -------------------- RIHANNA --------------------
    "Diamonds": [
        "Rihanna", "We Found Love", "Umbrella", "Shake It Off", "Rolling in the Deep"
    ],
    "We Found Love": [
        "Rihanna", "Diamonds", "Bad Blood", "Just the Way You Are", "Part of Me"
    ],
    "Umbrella": [
        "Rihanna", "Diamonds", "Rude Boy", "Dark Horse", "The Heart Wants What It Wants"
    ],
    "Only Girl (In the World)": [
        "Rihanna", "Work", "Firework", "No Tears Left to Cry", "Hotter Than Hell"
    ],
    "Stay": [
        "Rihanna", "Diamonds", "Sugar", "Set Fire to the Rain", "Galway Girl"
    ],
    "Work": [
        "Rihanna", "Only Girl (In the World)", "Shake It Off", "Trumpets", "Be the One"
    ],
    "Rude Boy": [
        "Rihanna", "Umbrella", "Physical", "Come & Get It", "Photograph"
    ],
    
    # -------------------- JASON DERULO --------------------
    "Trumpets": [
        "Jason Derulo", "Talk Dirty", "In My Head", "Work", "Bad Blood"
    ],
    "Want to Want Me": [
        "Jason Derulo", "Wiggle", "Levitating", "Shake It Off", "Locked Out of Heaven"
    ],
    "Talk Dirty": [
        "Jason Derulo", "Trumpets", "Wiggle", "Dark Horse", "Photograph"
    ],
    "Wiggle": [
        "Jason Derulo", "Talk Dirty", "Want to Want Me", "Sugar", "Me Too"
    ],
    "Ridin' Solo": [
        "Jason Derulo", "In My Head", "In My Blood", "Love Yourself", "Teenage Dream"
    ],
    "Marry Me": [
        "Jason Derulo", "Ridin' Solo", "Intentions", "Photograph", "Stitches"
    ],
    "In My Head": [
        "Jason Derulo", "Trumpets", "Ridin' Solo", "Shake It Off", "Delicate"
    ],
    
    # -------------------- SHAWN MENDES --------------------
    "Stitches": [
        "Shawn Mendes", "Treat You Better", "Mercy", "Marry Me", "The Heart Wants What It Wants"
    ],
    "Treat You Better": [
        "Shawn Mendes", "Stitches", "Senorita", "Shake It Off", "Galway Girl"
    ],
    "There's Nothing Holdin' Me Back": [
        "Shawn Mendes", "In My Blood", "Roar", "Rude Boy", "Levitating"
    ],
    "Senorita": [
        "Shawn Mendes", "Camila Cabello", "Bad Blood", "Havana", "Uptown Funk"
    ],
    "If I Can't Have You": [
        "Shawn Mendes", "In My Blood", "Delicate", "Want to Want Me", "Same Old Love"
    ],
    "Mercy": [
        "Shawn Mendes", "Stitches", "She Will Be Loved", "Love Story", "Sugar"
    ],
    "In My Blood": [
        "Shawn Mendes", "Mercy", "There's Nothing Holdin' Me Back", "If I Can't Have You",
        "What Do You Mean"
    ],
    
    # -------------------- CHARLIE PUTH --------------------
    "Attention": [
        "Charlie Puth", "We Don't Talk Anymore", "How Long", "Marry Me", 
        "Look What You Made Me Do"
    ],
    "We Don't Talk Anymore": [
        "Charlie Puth", "Love Yourself", "Attention", "She Will Be Loved", "Talk Dirty"
    ],
    "One Call Away": [
        "Charlie Puth", "How Long", "See You Again", "Photograph", "Hotter Than Hell"
    ],
    "How Long": [
        "Charlie Puth", "Attention", "One Call Away", "New Rules", "In My Blood"
    ],
    "Marvin Gaye": [
        "Charlie Puth", "Meghan Trainor", "No Tears Left to Cry", "Dark Horse",
        "Uptown Funk"
    ],
    "See You Again": [
        "Charlie Puth", "One Call Away", "Hello", "Roar", "Shake It Off"
    ],
    
    # -------------------- CAMILA CABELLO --------------------
    "Havana": [
        "Camila Cabello", "7 Rings", "Senorita", "Liar", "Delicate"
    ],
    "Never Be the Same": [
        "Camila Cabello", "Crying in the Club", "Break Free", "Girls Like You", 
        "I Don't Care"
    ],
    "Senorita": [
        "Camila Cabello", "Shawn Mendes", "Bad Blood", "Havana", "Uptown Funk"
    ],
    "Crying in the Club": [
        "Camila Cabello", "Never Be the Same", "I Have Questions", "Sorry", 
        "She Will Be Loved"
    ],
    "Liar": [
        "Camila Cabello", "Havana", "IDGAF", "Uptown Funk", "Stitches"
    ],
    "I Have Questions": [
        "Camila Cabello", "Crying in the Club", "Perfect", "Focus", 
        "I Knew You Were Trouble"
    ],
    
    # -------------------- LADY GAGA --------------------
    "Shallow": [
        "Lady Gaga", "Bradley Cooper", "Rain on Me", "Memories", "Hands to Myself"
    ],
    "Bad Romance": [
        "Lady Gaga", "Poker Face", "Telephone", "Blank Space", "Sorry"
    ],
    "Poker Face": [
        "Lady Gaga", "Bad Romance", "Born This Way", "Blank Space", "Sugar"
    ],
    "Born This Way": [
        "Lady Gaga", "Poker Face", "The Edge of Glory", "Shake It Off", 
        "No Tears Left to Cry"
    ],
    "Stupid Love": [
        "Lady Gaga", "Rain on Me", "Sugar", "Hotter Than Hell", "I Knew You Were Trouble"
    ],
    "Rain on Me": [
        "Lady Gaga", "Stupid Love", "Shallow", "Roar", "We Found Love"
    ],
    "The Edge of Glory": [
        "Lady Gaga", "Born This Way", "Dark Horse", "Galway Girl", "Baby"
    ],
    "Telephone": [
        "Lady Gaga", "Bad Romance", "Shake It Off", "No Tears Left to Cry", "New Rules"
    ],
    
    # -------------------- ADELE --------------------
    "Rolling in the Deep": [
        "Adele", "Someone Like You", "Skyfall", "Diamonds", "Uptown Funk"
    ],
    "Someone Like You": [
        "Adele", "When We Were Young", "Rolling in the Deep", "See You Again", "Sugar"
    ],
    "Hello": [
        "Adele", "Set Fire to the Rain", "See You Again", "Sugar", "Poker Face"
    ],
    "Set Fire to the Rain": [
        "Adele", "Hello", "When We Were Young", "Stay", "Shallow"
    ],
    "When We Were Young": [
        "Adele", "Someone Like You", "Set Fire to the Rain", "Part of Me", 
        "No Tears Left to Cry"
    ],
    "Send My Love (To Your New Lover)": [
        "Adele", "Rolling in the Deep", "Hello", "Havana", "Sorry"
    ],
    "Skyfall": [
        "Adele", "Rolling in the Deep", "Shake It Off", "Senorita", "Animals"
    ],
    
    # -------------------- ONE DIRECTION --------------------
    "What Makes You Beautiful": [
        "One Direction", "Best Song Ever", "One Thing", "Dark Horse", "Marry Me"
    ],
    "Story of My Life": [
        "One Direction", "Drag Me Down", "Havana", "Delicate", "Trumpets"
    ],
    "Drag Me Down": [
        "One Direction", "Story of My Life", "Best Song Ever", "Sugar", "IDGAF"
    ],
    "Best Song Ever": [
        "One Direction", "What Makes You Beautiful", "Drag Me Down", 
        "Bad Romance", "Girls Like You"
    ],
    "Little Things": [
        "One Direction", "One Thing", "We Found Love", "Galway Girl", "In My Head"
    ],
    "One Thing": [
        "One Direction", "What Makes You Beautiful", "Little Things", "Photograph", 
        "Havana"
    ],
    
    # -------------------- BILLIE EILISH --------------------
    "Bad Guy": [
        "Billie Eilish", "Ocean Eyes", "When the Party's Over", "Baby", "Blank Space"
    ],
    "Ocean Eyes": [
        "Billie Eilish", "Everything I Wanted", "Bad Guy", "Stay", "Focus"
    ],
    "Everything I Wanted": [
        "Billie Eilish", "Ocean Eyes", "Bury a Friend", "Photograph", "We Found Love"
    ],
    "Bury a Friend": [
        "Billie Eilish", "Everything I Wanted", "Mercy", "Shallow", "Delicate"
    ],
    "When the Party's Over": [
        "Billie Eilish", "Bad Guy", "Liar", "Stitches", "Dark Horse"
    ],
    "Lovely": [
        "Billie Eilish", "Khalid", "Shake It Off", "Focus", "No"
    ],
    
    # -------------------- TROYE SIVAN --------------------
    "Youth": [
        "Troye Sivan", "My My My!", "Wild", "Senorita", "No Tears Left to Cry"
    ],
    "My My My!": [
        "Troye Sivan", "Youth", "Bloom", "Havana", "We Don't Talk Anymore"
    ],
    "Wild": [
        "Troye Sivan", "Youth", "Talk Me Down", "Dark Horse", "Skyfall"
    ],
    "Talk Me Down": [
        "Troye Sivan", "Wild", "My My My!", "Just the Way You Are", "Focus"
    ],
    "Strawberries & Cigarettes": [
        "Troye Sivan", "Bloom", "See You Again", "Delicate", "We Found Love"
    ],
    "Bloom": [
        "Troye Sivan", "My My My!", "Strawberries & Cigarettes", "Part of Me", 
        "Only Girl (In the World)"
    ],
    
    # -------------------- MEGHAN TRAINOR --------------------
    "All About That Bass": [
        "Meghan Trainor", "Lips Are Movin", "Lose You to Love Me", "Story of My Life",
        "Ridin' Solo"
    ],
    "Like I'm Gonna Lose You": [
        "Meghan Trainor", "Marvin Gaye", "Shake It Off", "In My Head", "Rude Boy"
    ],
    "No": [
        "Meghan Trainor", "Lips Are Movin", "Lovely", "Blank Space", "Hotter Than Hell"
    ],
    "Lips Are Movin": [
        "Meghan Trainor", "All About That Bass", "No", "Wiggle", "Delicate"
    ],
    "Dear Future Husband": [
        "Meghan Trainor", "All About That Bass", "Moves Like Jagger", "Photograph", 
        "Focus"
    ],
    "Me Too": [
        "Meghan Trainor", "Dear Future Husband", "Wiggle", "Payphone", 
        "California Gurls"
    ],
    
    # -------------------- CARLY RAE JEPSEN --------------------
    "Call Me Maybe": [
        "Carly Rae Jepsen", "I Really Like You", "Sugar", "22", "Break Free"
    ],
    "I Really Like You": [
        "Carly Rae Jepsen", "Call Me Maybe", "Run Away with Me", "Shake It Off", 
        "We Found Love"
    ],
    "Run Away with Me": [
        "Carly Rae Jepsen", "I Really Like You", "Cut to the Feeling", 
        "Look What You Made Me Do", "Dark Horse"
    ],
    "Good Time": [
        "Carly Rae Jepsen", "Owl City", "Moves Like Jagger", "Baby", "Blank Space"
    ],
    "Cut to the Feeling": [
        "Carly Rae Jepsen", "Run Away with Me", "Treasure", "Photograph", 
        "Lips Are Movin"
    ]
}
