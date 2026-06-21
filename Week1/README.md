## Task 1 

```
    def __new__(cls):
        if cls._instance is None:  
            cls._instance = super().__new__(cls)
        return cls._instance
```

-> _instance is a class variable that stores the single object.

-> Initially _instance is None because no object exists yet.

-> cls refers to the class itself.

-> __new__() is overridden to control object creation.

-> If no instance exists, a new object is created and stored.

-> Otherwise, the existing object is returned.

# output
![alt text](image.png)



## Task 2

```

```