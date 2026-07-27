# Pydantic notes : 
- youtube link: https://www.youtube.com/watch?v=M81pfi64eeM&list=PL1pUCNO-yV2nJGCS4O0_rJUJbJMEPfsvk
- made on nov 2025 

### what is do ? : 
> it make sure that the data comming in the DB meet certain expectaion such as type and format of the data 
- its usage: 
    - Fast api is used this for validataing the data input from api requests 
    - used in data processing tools 
    - used where the data go to a system 
    - pydantic AI is used for AI tools 
- why don't we write type of data on out own? 
    - if the any error is therewe will getting one error at a time about the type 
    - using pydantic we get all the error at a same time in one run so it will help us to write efficent code 
    >  it is because pydantic has type conversion enable by default and it sometime convert the suitatble type coversion , which has less memory usage. 
    > we have to make sure the size of the data

* 
    datetime.now(UTC) # it will call datetime once when class is created but we need call every time when a instance is created.
    - we can make it easy by using lambda fucntion
    - we can use partial () from functool
