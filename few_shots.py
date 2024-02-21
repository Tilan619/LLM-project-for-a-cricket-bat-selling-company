few_shots = [
    {'Question' : "How many bats do we have left for ss in size 5",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM bats WHERE brand = 'SS' AND size = 'Size 5'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '163'},
    {'Question': "How much is the price of the inventory for all small adult size bats?",
     'SQLQuery':"SELECT SUM(price*stock_quantity) FROM bats WHERE size = 'Small Adult'",
     'SQLResult': "Result of the SQL query",
     'Answer': '86292'},
    {'Question': "If we have to sell all the SS bats today with discounts applied. How much revenue our store will generate (post discounts)?",
     'SQLQuery' : "select sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from (select sum(price*stock_quantity) as total_amount, bat_id from bats where brand = 'SS' group by bat_id) a left join discounts on a.bat_id = discounts.bat_id",
     'SQLResult': "Result of the SQL query",
     'Answer': '88274.1'} ,
     {'Question' : "how much we can make by selling all sg bats without discounts?" ,
      'SQLQuery': "SELECT SUM(price * stock_quantity) FROM bats WHERE brand = 'SG'",
      'SQLResult': "Result of the SQL query",
      'Answer' : '71210'},
    {'Question': "How many grey niccols bats we have available?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM bats WHERE brand = 'Gray Nicolls'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '602'
     },
    {'Question': "how many ss orange color size 5 bats do we have?",
     'SQLQuery' : "SELECT stock_quantity FROM bats WHERE brand = 'SS' AND label_color = 'Orange' AND size = 'Size 5'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '79'
     },
    {'Question': "what is the total revenue we can get by selling ss blue color sfull size bats without discounts?",
     'SQLQuery' : "SELECT (price*stock_quantity) FROM bats WHERE brand='SS' AND label_color = 'Blue' AND size = 'Full Size'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '10720'
     },
    {'Question': "what is the total revenue we can get by selling sg full size bats without discounts?",
     'SQLQuery' : "SELECT SUM(price*stock_quantity) FROM bats WHERE brand = 'SG' AND size = 'Full Size'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '12737'
     },
    {'Question': "how much money can we make if we sell all gray nicolls bats?",
     'SQLQuery' : "SELECT SUM(price*stock_quantity) FROM bats WHERE brand = 'Gray Nicolls'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '71604'
     },
    {'Question': "how much money can we make if we sell all orange small adult bats without discounts?",
     'SQLQuery' : "SELECT SUM(price*stock_quantity) FROM bats WHERE label_color = 'Orange' AND size = 'Small Adult'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '25671'
     },
    {'Question': "what is the revenue of selling blue color bats?",
     'SQLQuery' : "SELECT SUM(price*stock_quantity) FROM bats WHERE label_color = 'Blue'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '102049'
     },
    {'Question': "what is the quantity we have in mrf blue color bats?",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM bats WHERE brand = 'MRF' AND label_color = 'Blue'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '230'
     },
    {'Question': "what is the quantity we have in red size 5 bats?",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM bats WHERE label_color = 'Red' AND size = 'Size 5'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '251'
     },
    {'Question': "how many red bats we have?",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM bats WHERE label_color = 'Red'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '1026'
     },
    {'Question': "how many harrow bats we have?",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM bats WHERE size = 'Harrow'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '603'
     }
]