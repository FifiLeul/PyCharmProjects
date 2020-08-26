from random import randint

class Generator:
    unwatched_content = []

    def __init__(self, content = None, content_type = None):
        self.content = self.lst_to_strs(content)
        self.unwatched_content = content
        self.amount_of_content = len(self.content)
        self.content_type = content_type

    def lst_to_strs(self, content):
        content = content.splitlines()
        #print(content)
        for i in range(len(content)):
           title = content[i]
           title = title.split(" ")
           str = ""
           for word in title:
            word = word.capitalize()
            str += word + " "
           title = str
           #print(title)
           content[i] = title
       # print(content)

        return ["\"{}\"".format(movie) for movie in content]

    def add(self, content):
        self.content.append(content)
        self.amount_of_content += 1
        print("Just added {}!".format(self.content[self.amount_of_content]))
    def generate(self):
        print("You're going to watch the {""} {}!!".format(self.content_type, self.content[randint(0, self.amount_of_content)]))

movies_lst = "Marriage story\n" \
             "Boyhood\n" \
             "Edge of seventeen\n" \
             "Freaks\n" \
             "All the bright places\n" \
             "Me and earl and the dying girl\n" \
             "Get out\n" \
             "perks of being a wallflower\n" \
             "Baby driver\n" \
             "The interview\n" \
             "Ratatouille\n" \
             "Parasite\n" \
             "Joker\n" \
             "Tigertail\n" \
             "The farewell\n" \
             "The great gatsby\n" \
             "Crazy rich Asians\n" \
             "Dead poets society\n" \
             "Love, rosie\n" \
             "Love, Simon\n" \
             "Infinity war\n" \
             "Tangled\n" \
             "The devil wears Prada\n" \
             "The lovebirds\n" \
             "I, tonya\n" \
             "The wolf of wallstreet\n" \
             "Us\n" \
             "Hunt for the wilder people\n"\
             "Just mercy\n" \
             "Mid 90’s: frances\n" \
             "Fill metal jacket: stein\n" \
             "Fight club; Percy\n" \
             "The guest: percy\n" \
             "Teddy bear crisis: ski movie on Vimeo for free\n" \
             "Lady bird; anastasia\n" \
             "28 days later: Ella\n" \
             "Moonrise kindom : Maya\n" \
             "Big sick: Maya\n" \
             "Extremely wicked: maya\n" \
             "A beautiful mind: kyleb\n" \
             "Pursuit of happiness: Sara\n" \
             "To the bone: Sara\n" \
             "Now you see me: Sara\n" \
             "Red dawn: Sara\n" \
             "Little women: Lia\n" \
             "10 things I hate about you: lia\n" \
             "Synecdoche\n" \
             "Blade runner\n" \
             "Midsommar\n" \
             "8 1/2\n" \
             "Mother!\n" \
             "The Truman show\n" \
             "Gone girl\n" \
             "Interstellar\n" \
             "The shape of water\n" \
             "Moonlight\n" \
             "13th\n" \
             "Selma\n" \
             "If beatle street could talk\n" \
             "Whiplash\n" \
             "The last black man in San Francisco\n" \
             "Her: spike jonze\n" \
             "The umbrellas of sonbourg\n" \
             "Amadeus\n" \
             "Ferris maulers day off\n" \
             "Back to the future\n" \
             "Raiders of the lost ark\n" \
             "Do the right thing\n" \
             "The shining\n" \
             "La Jaime\n" \
             "Amelie\n" \
             "The dreamers\n" \
             "Ratatouille\n" \
             "Titanic\n" \
             "Les miserables\n" \
             "Suspiria\n" \
             "Split\n" \
             "Brooklyn\n" \
             "Catch me if you can\n" \
             "Grand Budapest hotel\n" \
             "To kill a mockingbird\n" \
             "Moonrise kingdom\n" \
             "To catch a thief\n" \
             "A clockwork orange\n" \
             "1963\n" \
             "Scott pilgrim v the world\n" \
             "Spider man into the spider verse\n" \
             "V for vendetta\n" \
             "Raiders of the lost ark\n" \
             "Dolemite is my name\n" \
             "Groundhog Day\n" \
             "Blue valentine\n" \
             "Terminal\n" \
             "Bombshell\n" \
             "Scream\n" \
             "beasts of no nation\n" \
             "mississippi burning\n" \
             "Maurice\n" \
             "Virgin Suicides\n" \
             "Eternal Sunshine of the Spotless Mind\n" \
             "Before Sunrise\n" \
             "Honey Boy\n" \
             "Uncut Gems\n" \
             "Dunkirk\n"
movie_generator = Generator(movies_lst, "movie")
movie_generator.generate()