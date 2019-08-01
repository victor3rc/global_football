"""
This module contains the teams which played in each world cup, along with the information for
where players in their squads were based at the time of the world cup.

This information was sourced from:

https://en.wikipedia.org/wiki/1930_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1934_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1938_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1950_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1930_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1958_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1962_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1966_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1970_FIFA_World_Cup_squads
"""
from collections import namedtuple


Squad = namedtuple('Squad', 'immigrants emigrated_country emigrated_confederation total')

# South America - CONMENBOL
ARGENTINA = {1930: Squad(0, 0, 0, 23), 1934: Squad(0, 0, 0, 18), 1958: Squad(0, 0, 0, 22),
             1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22), 1974: Squad(1, 6, 5, 22),
             1978: Squad(0, 1, 1, 22), 1982: Squad(0, 3, 3, 22), 1986: Squad(4, 7, 6, 22)}
CHILE = {1930: Squad(0, 0, 0, 19), 1950: Squad(0, 1, 1, 22), 1962: Squad(0, 0, 0, 22),
         1966: Squad(0, 0, 0, 22), 1974: Squad(0, 6, 5, 22), 1982: Squad(0, 0, 0, 22)}
BRAZIL = {1930: Squad(0, 0, 0, 22), 1934: Squad(0, 2, 0, 19), 1938: Squad(0, 0, 0, 22),
          1950: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22), 1958: Squad(0, 0, 0, 22),
          1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22), 1970: Squad(0, 0, 0, 22),
          1974: Squad(5, 0, 0, 22), 1978: Squad(0, 0, 0, 22), 1982: Squad(0, 2, 2, 22),
          1986: Squad(5, 2, 2, 22)}
BOLIVIA = {1930: Squad(0, 0, 0, 17), 1950: Squad(0, 0, 0, 22)}
URUGUAY = {1930: Squad(0, 0, 0, 22), 1934: Squad(2, 0, 0, 0), 1950: Squad(0, 0, 0, 22),
           1954: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
           1970: Squad(0, 0, 0, 22), 1974: Squad(0, 6, 1, 22), 1986: Squad(0, 13, 4, 22)}
PERU = {1930: Squad(0, 0, 0, 20), 1970: Squad(0, 0, 0, 22), 1974: Squad(1, 0, 0, 0),
        1978: Squad(0, 1, 1, 22), 1982: Squad(0, 7, 4, 22)}
PARAGUAY = {1930: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22), 1958: Squad(0, 0, 0, 22),
            1986: Squad(0, 7, 1, 22)}
COLOMBIA = {1962: Squad(0, 0, 0, 22), 1982: Squad(3, 0, 0, 0), 1986: Squad(6, 0, 0, 0)}

# Central and North America - CONCACAF
MEXICO = {1930: Squad(1, 0, 0, 17), 1950: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
          1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
          1970: Squad(0, 0, 0, 22), 1974: Squad(4, 0, 0, 0), 1978: Squad(1, 0, 0, 22),
          1982: Squad(1, 0, 0, 0), 1986: Squad(3, 1, 1, 22)}
USA = {1930: Squad(0, 0, 0, 16), 1934: Squad(0, 0, 0, 19), 1950: Squad(0, 0, 0, 19),
       1982: Squad(3, 0, 0, 0), 1986: Squad(10, 0, 0, 0)}
CUBA = {1938: Squad(0, 0, 0, 22)}
EL_SALVADOR = {1970: Squad(0, 0, 0, 22), 1982: Squad(0, 1, 1, 22)}
HAITI = {1974: Squad(0, 2, 1, 22)}
TRINIDAD = {1974: Squad(1, 0, 0, 0)}
HONDURAS = {1982: Squad(0, 1, 1, 22)}
CANADA = {1982: Squad(1, 0, 0, 0), 1986: Squad(0, 16, 5, 22)}

# Europe - UEFA
FRANCE = {1930: Squad(3, 0, 0, 16), 1934: Squad(1, 0, 0, 22), 1938: Squad(3, 0, 0, 22),
          1954: Squad(0, 0, 0, 22), 1958: Squad(0, 1, 0, 22), 1962: Squad(2, 0, 0, 0),
          1966: Squad(0, 2, 0, 22), 1974: Squad(3, 0, 0, 0), 1978: Squad(2, 0, 0, 22),
          1982: Squad(17, 0, 0, 22), 1986: Squad(16, 2, 0, 22)}
YUGOSLAVIA = {1930: Squad(0, 3, 0, 17), 1950: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
              1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1974: Squad(0, 1, 0, 22),
              1982: Squad(0, 6, 0, 22)}
ROMANIA = {1930: Squad(0, 0, 0, 15), 1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22),
           1970: Squad(0, 0, 0, 22)}
BELGIUM = {1930: Squad(0, 0, 0, 16), 1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22),
           1954: Squad(0, 0, 0, 22), 1970: Squad(4, 0, 0, 22), 1974: Squad(2, 0, 0, 0),
           1978: Squad(6, 0, 0, 0), 1982: Squad(7, 2, 0, 22), 1986: Squad(6, 2, 0, 22)}
AUSTRIA = {1934: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22), 1958: Squad(0, 0, 0, 22),
           1978: Squad(0, 5, 0, 22), 1982: Squad(1, 6, 0, 22)}
CZECHOSLOVAKIA = {1934: Squad(0, 1, 0, 22), 1938: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
                  1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1970: Squad(0, 1, 0, 22),
                  1982: Squad(0, 1, 0, 22)}
GERMANY = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
           1958: Squad(0, 0, 0, 22), 1962: Squad(0, 1, 0, 22), 1966: Squad(0, 3, 0, 22),
           1970: Squad(0, 2, 0, 22), 1974: Squad(3, 1, 0, 22), 1978: Squad(8, 0, 0, 22),
           1982: Squad(5, 1, 0, 22), 1986: Squad(2, 2, 0, 22)}
EAST_GERMANY = {1974: Squad(0, 0, 0, 22)}
HUNGARY = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 1, 0, 22), 1954: Squad(0, 0, 0, 22),
           1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
           1978: Squad(0, 0, 0, 22), 1982: Squad(0, 5, 0, 22), 1986: Squad(0, 3, 0, 22)}
ITALY = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22),
         1954: Squad(0, 0, 0, 22), 1958: Squad(6, 0, 0, 0), 1962: Squad(4, 0, 0, 22),
         1966: Squad(7, 0, 0, 22), 1970: Squad(2, 0, 0, 22), 1974: Squad(0, 0, 0, 22),
         1978: Squad(0, 0, 0, 22), 1982: Squad(5, 0, 0, 22), 1986: Squad(16, 0, 0, 22)}
SPAIN = {1934: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22), 1958: Squad(1, 0, 0, 0),
         1962: Squad(0, 0, 0, 22), 1966: Squad(1, 3, 0, 22), 1974: Squad(7, 0, 0, 0),
         1978: Squad(2, 0, 0, 22), 1982: Squad(8, 0, 0, 22), 1986: Squad(6, 0, 0, 22)}
SWEDEN = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22),
          1958: Squad(0, 5, 0, 22), 1970: Squad(0, 6, 0, 22), 1974: Squad(0, 6, 0, 22),
          1978: Squad(0, 6, 0, 22)}
SWITZERLAND = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 2, 0, 22), 1950: Squad(0, 0, 0, 22),
               1954: Squad(0, 0, 0, 22), 1962: Squad(0, 3, 0, 22), 1966: Squad(0, 0, 0, 22),
               1970: Squad(1, 0, 0, 0), 1974: Squad(1, 0, 0, 0), 1978: Squad(1, 0, 0, 0),
               1982: Squad(2, 0, 0, 0), 1986: Squad(4, 0, 0, 0)}
POLAND = {1938: Squad(0, 0, 0, 22), 1974: Squad(0, 0, 0, 22), 1978: Squad(0, 1, 0, 22),
          1986: Squad(0, 4, 0, 22)}
NORWAY = {1938: Squad(0, 0, 0, 22), 1982: Squad(0, 2, 0, 22)}
NETHERLANDS = {1938: Squad(0, 0, 0, 22), 1970: Squad(1, 0, 0, 0), 1974: Squad(0, 3, 0, 22),
               1978: Squad(1, 6, 0, 22), 1986: Squad(6, 0, 0, 0)}
ENGLAND = {1950: Squad(1, 0, 0, 22), 1954: Squad(7, 0, 0, 22), 1958: Squad(35, 0, 0, 22),
           1962: Squad(0, 1, 0, 22), 1966: Squad(0, 0, 0, 22), 1970: Squad(0, 0, 0, 22),
           1974: Squad(12, 0, 0, 0), 1978: Squad(15, 0, 0, 0), 1982: Squad(29, 0, 0, 22),
           1986: Squad(31, 0, 0, 22)}
TURKEY = {1954: Squad(0, 0, 0, 22), 1986: Squad(1, 0, 0, 0)}
SCOTLAND = {1954: Squad(0, 7, 0, 22), 1958: Squad(2, 6, 0, 22), 1970: Squad(1, 0, 0, 0),
            1974: Squad(0, 12, 0, 22), 1978: Squad(0, 15, 0, 22), 1982: Squad(1, 13, 0, 22),
            1986: Squad(1, 9, 0, 22)}
NORTHERN_IRELAND = {1958: Squad(0, 19, 0, 22), 1982: Squad(0, 18, 2, 22),
                    1986: Squad(0, 20, 0, 22)}
WALES = {1958: Squad(0, 13, 0, 22)}
SOVIET_UNION = {1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
                1970: Squad(0, 0, 0, 22), 1982: Squad(0, 0, 0, 22), 1986: Squad(0, 0, 0, 22)}
BULGARIA = {1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22), 1970: Squad(0, 0, 0, 22),
            1974: Squad(0, 0, 0, 22), 1986: Squad(0, 2, 0, 22)}
PORTUGAL = {1966: Squad(0, 0, 0, 22), 1974: Squad(1, 0, 0, 0), 1982: Squad(1, 0, 0, 0),
            1986: Squad(2, 0, 0, 22)}
ISRAEL = {1970: Squad(0, 0, 0, 22)}
DENMARK = {1986: Squad(0, 15, 0, 22)}
GREECE = {1986: Squad(1, 0, 0, 0)}

# Africa -
EGYPT = {1934: Squad(0, 0, 0, 20)}
MOROCCO = {1970: Squad(0, 0, 0, 19), 1986: Squad(0, 5, 5, 22)}
ZAIRE = {1974: Squad(0, 0, 0, 22)}
TUNISIA = {1978: Squad(0, 2, 2, 22)}
CAMEROON = {1982: Squad(0, 6, 5, 22)}
ALGERIA = {1982: Squad(0, 7, 7, 22), 1986: Squad(0, 11, 11, 22)}
IVORY_COAST = {1982: Squad(1, 0, 0, 0)}

# Asia & Oceania -
DUTCH_EAST_INDIES = {1938: Squad(0, 0, 0, 17)}
SOUTH_KOREA = {1954: Squad(0, 0, 0, 20), 1986: Squad(0, 1, 1, 22)}
NORTH_KOREA = {1966: Squad(0, 0, 0, 22)}
AUSTRALIA = {1974: Squad(0, 0, 0, 22)}
IRAN = {1978: Squad(0, 0, 0, 22)}
SAUDI_ARABIA = {1978: Squad(1, 0, 0, 0)}
KUWAIT = {1982: Squad(0, 0, 0, 22)}
NEW_ZEALAND = {1982: Squad(0, 0, 0, 22)}
IRAQ = {1986: Squad(0, 0, 0, 22)}
