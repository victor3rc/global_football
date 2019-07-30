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
"""
from collections import namedtuple


Players = namedtuple('Players', 'other_country other_confederation total')

# South America - CONMENBOL
ARGENTINA = {1930: Players(0, 0, 23), 1934: Players(0, 0, 18), 1958: Players(0, 0, 22),
             1962: Players(0, 0, 22)}
CHILE = {1930: Players(0, 0, 19), 1950: Players(1, 1, 22), 1962: Players(0, 0, 22)}
BRAZIL = {1930: Players(0, 0, 22), 1934: Players(2, 0, 19), 1938: Players(0, 0, 22),
          1950: Players(0, 0, 22), 1954: Players(0, 0, 22), 1958: Players(0, 0, 22),
          1962: Players(0, 0, 22)}
BOLIVIA = {1930: Players(0, 0, 17), 1950: Players(0, 0, 22)}
URUGUAY = {1930: Players(0, 0, 22), 1950: Players(0, 0, 22), 1954: Players(0, 0, 22),
           1962: Players(0, 0, 22)}
PERU = {1930: Players(0, 0, 20)}
PARAGUAY = {1930: Players(0, 0, 22), 1950: Players(0, 0, 22), 1958: Players(0, 0, 22)}
COLOMBIA = {1962: Players(0, 0, 22)}

# Central and North America - CONCACAF
MEXICO = {1930: Players(0, 0, 17), 1950: Players(0, 0, 22), 1954: Players(0, 0, 22),
          1958: Players(0, 0, 22), 1962: Players(0, 0, 22)}
USA = {1930: Players(0, 0, 16), 1934: Players(0, 0, 19), 1950: Players(0, 0, 19)}
CUBA = {1938: Players(0, 0, 22)}

# Europe - UEFA
FRANCE = {1930: Players(0, 0, 16), 1934: Players(0, 0, 22), 1938: Players(0, 0, 22),
          1954: Players(0, 0, 22), 1958: Players(1, 0, 22)}
YUGOSLAVIA = {1930: Players(3, 0, 17), 1950: Players(0, 0, 22), 1954: Players(0, 0, 22),
              1958: Players(0, 0, 22), 1962: Players(0, 0, 22)}
ROMANIA = {1930: Players(0, 0, 15), 1934: Players(0, 0, 22), 1938: Players(0, 0, 22)}
BELGIUM = {1930: Players(0, 0, 16), 1934: Players(0, 0, 22), 1938: Players(0, 0, 22),
           1954: Players(0, 0, 22)}
AUSTRIA = {1934: Players(0, 0, 22), 1954: Players(0, 0, 22), 1958: Players(0, 0, 22)}
CZECHOSLOVAKIA = {1934: Players(1, 0, 22), 1938: Players(0, 0, 22), 1954: Players(0, 0, 22),
                  1958: Players(0, 0, 22), 1962: Players(0, 0, 22)}
GERMANY = {1934: Players(0, 0, 22), 1938: Players(0, 0, 22), 1954: Players(0, 0, 22),
           1958: Players(0, 0, 22), 1962: Players(1, 0, 22)}
HUNGARY = {1934: Players(0, 0, 22), 1938: Players(1, 0, 22), 1954: Players(0, 0, 22),
           1958: Players(0, 0, 22), 1962: Players(0, 0, 22)}
ITALY = {1934: Players(0, 0, 22), 1938: Players(0, 0, 22), 1950: Players(0, 0, 22),
         1954: Players(0, 0, 22), 1962: Players(0, 0, 22)}
SPAIN = {1934: Players(0, 0, 22), 1950: Players(0, 0, 22), 1962: Players(0, 0, 22)}
SWEDEN = {1934: Players(0, 0, 22), 1938: Players(0, 0, 22), 1950: Players(0, 0, 22),
          1958: Players(5, 0, 22)}
SWITZERLAND = {1934: Players(0, 0, 22), 1938: Players(2, 0, 22), 1950: Players(0, 0, 22),
               1954: Players(0, 0, 22), 1962: Players(3, 0, 22)}
POLAND = {1938: Players(0, 0, 22)}
NORWAY = {1938: Players(0, 0, 22)}
NETHERLANDS = {1938: Players(0, 0, 22)}
ENGLAND = {1950: Players(0, 0, 22), 1954: Players(0, 0, 22), 1958: Players(0, 0, 22),
           1962: Players(1, 0, 22)}
TURKEY = {1954: Players(0, 0, 22)}
SCOTLAND = {1954: Players(7, 0, 22), 1958: Players(6, 0, 22)}
NORTHERN_IRELAND = {1958: Players(19, 0, 22)}
WALES = {1958: Players(13, 0, 22)}
SOVIET_UNION = {1958: Players(0, 0, 22), 1962: Players(0, 0, 22)}
BULGARIA = {1962: Players(0, 0, 22)}

# Africa -
EGYPT = {1934: Players(0, 0, 20)}

# Asia -
DUTCH_EAST_INDIES = {1938: Players(0, 0, 17)}
SOUTH_KOREA = {1954: Players(0, 0, 20)}

