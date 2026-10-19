import connect
from models import Quote, Author
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

@cache
def name(data):
    print("Func call")
    quotes=Quote.objects(author=Author.objects(fullname=data).first())
    quotes_list=[]
    for quote in quotes:
        quotes_list.append(quote.quote)
    return(quotes_list)
    
def main():
    while True:
        text=input("commands: \nname:(author name) \ntag:(some tag) \ntags:(some tag1),(some tag2)\nexit\n")
        data=text.split(":")

        if data[0].lower()=="name":
            print(name(data[1]))

        elif data[0].lower()=="tag":
            quotes=Quote.objects(tags=data[1])
            quotes_list=[]
            for quote in quotes:
                quotes_list.append(quote.quote)
            print(quotes_list)

        elif data[0].lower()=="tags":
            tags=data[1].split(",")        
            quotes=Quote.objects(tags__in=tags)
            quotes_list=[]
            for quote in quotes:
                quotes_list.append(quote.quote)
            print(quotes_list)

        elif data[0].lower()=="exit":
            break

        else:
            print("Unknown command")
            
if __name__=="__main__":
    main()