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
https://en.wikipedia.org/wiki/1974_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1978_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1982_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1986_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1990_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1994_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/1998_FIFA_World_Cup_squads
https://en.wikipedia.org/wiki/2002_FIFA_World_Cup_squads
"""
from collections import namedtuple


Squad = namedtuple('Squad', 'immigrants emigrated_country emigrated_confederation total')

# South America - CONMENBOL
ARGENTINA = {1930: Squad(0, 0, 0, 23), 1934: Squad(0, 0, 0, 18), 1958: Squad(0, 0, 0, 22),
             1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22), 1974: Squad(1, 6, 5, 22),
             1978: Squad(0, 1, 1, 22), 1982: Squad(0, 3, 3, 22), 1986: Squad(4, 7, 6, 22),
             1990: Squad(2, 14, 13, 22), 1994: Squad(2, 11, 10, 22), 1998: Squad(14, 16, 16, 22),
             2002: Squad(3, 21, 20, 23), 2006: Squad(5, 20, 18, 23), 2010: Squad(5, 17, 17, 23),
             2014: Squad(4, 20, 20, 23)}
CHILE = {1930: Squad(0, 0, 0, 19), 1950: Squad(0, 1, 1, 22), 1962: Squad(0, 0, 0, 22),
         1966: Squad(0, 0, 0, 22), 1974: Squad(0, 6, 5, 22), 1982: Squad(0, 0, 0, 22),
         1994: Squad(3, 0, 0, 0), 1998: Squad(0, 4, 3, 22), 2002: Squad(1, 0, 0, 0),
         2010: Squad(3, 16, 14, 23), 2014: Squad(0, 18, 15, 23)}
BRAZIL = {1930: Squad(0, 0, 0, 22), 1934: Squad(0, 2, 0, 19), 1938: Squad(0, 0, 0, 22),
          1950: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22), 1958: Squad(0, 0, 0, 22),
          1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22), 1970: Squad(0, 0, 0, 22),
          1974: Squad(5, 0, 0, 22), 1978: Squad(0, 0, 0, 22), 1982: Squad(0, 2, 2, 22),
          1986: Squad(5, 2, 2, 22), 1990: Squad(0, 12, 0, 22), 1994: Squad(1, 11, 11, 22),
          1998: Squad(6, 13, 13, 22), 2002: Squad(2, 10, 10, 23), 2006: Squad(4, 20, 20, 23),
          2010: Squad(3, 20, 20, 23), 2014: Squad(7, 19, 19, 23)}
BOLIVIA = {1930: Squad(0, 0, 0, 17), 1950: Squad(0, 0, 0, 22), 1994: Squad(0, 7, 1, 22)}
URUGUAY = {1930: Squad(0, 0, 0, 22), 1934: Squad(2, 0, 0, 0), 1950: Squad(0, 0, 0, 22),
           1954: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
           1970: Squad(0, 0, 0, 22), 1974: Squad(0, 6, 1, 22), 1986: Squad(0, 13, 4, 22),
           1990: Squad(0, 12, 9, 22), 2002: Squad(0, 15, 15, 23), 2010: Squad(0, 21, 15, 23),
           2014: Squad(0, 22, 18, 23)}
PERU = {1930: Squad(0, 0, 0, 20), 1970: Squad(0, 0, 0, 22), 1974: Squad(1, 0, 0, 0),
        1978: Squad(0, 1, 1, 22), 1982: Squad(0, 7, 4, 22)}
PARAGUAY = {1930: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22), 1958: Squad(0, 0, 0, 22),
            1986: Squad(0, 7, 1, 22), 1998: Squad(0, 19, 7, 22), 2002: Squad(0, 14, 5, 23),
            2006: Squad(0, 18, 8, 23), 2010: Squad(0, 19, 13, 23), 2014: Squad(1, 0, 0, 0)}
COLOMBIA = {1962: Squad(0, 0, 0, 22), 1982: Squad(3, 0, 0, 0), 1986: Squad(6, 0, 0, 0),
            1990: Squad(1, 2, 2, 22), 1994: Squad(3, 4, 2, 22), 1998: Squad(0, 12, 4, 22),
            2010: Squad(2, 0, 0, 0), 2014: Squad(1, 20, 16, 23)}
ECUADOR = {1998: Squad(1, 0, 0, 0), 2002: Squad(0, 3, 3, 23), 2006: Squad(0, 5, 4, 23),
           2010: Squad(1, 0, 0, 0), 2014: Squad(0, 15, 13, 23)}

# Central and North America - CONCACAF
MEXICO = {1930: Squad(1, 0, 0, 17), 1950: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
          1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
          1970: Squad(0, 0, 0, 22), 1974: Squad(4, 0, 0, 0), 1978: Squad(1, 0, 0, 22),
          1982: Squad(1, 0, 0, 0), 1986: Squad(3, 1, 1, 22), 1990: Squad(2, 0, 0, 0),
          1994: Squad(1, 2, 2, 22), 1998: Squad(5, 1, 0, 22), 2002: Squad(6, 4, 4, 23),
          2006: Squad(4, 19, 18, 23), 2010: Squad(7, 9, 9, 23), 2014: Squad(9, 8, 8, 23)}
USA = {1930: Squad(0, 0, 0, 16), 1934: Squad(0, 0, 0, 19), 1950: Squad(0, 0, 0, 19),
       1982: Squad(3, 0, 0, 0), 1986: Squad(10, 0, 0, 0), 1990: Squad(0, 4, 4, 22),
       1994: Squad(0, 7, 6, 22), 1998: Squad(5, 6, 6, 22), 2002: Squad(0, 12, 12, 23),
       2006: Squad(3, 12, 12, 23), 2010: Squad(3, 19, 17, 23), 2014: Squad(9, 0, 0, 0)}
CUBA = {1938: Squad(0, 0, 0, 22)}
EL_SALVADOR = {1970: Squad(0, 0, 0, 22), 1982: Squad(0, 1, 1, 22)}
HAITI = {1974: Squad(0, 2, 1, 22)}
TRINIDAD = {1974: Squad(1, 0, 0, 0), 2006: Squad(0, 19, 17, 23)}
HONDURAS = {1982: Squad(0, 1, 1, 22), 2010: Squad(0, 9, 8, 23), 2014: Squad(0, 12, 7, 23)}
CANADA = {1982: Squad(1, 0, 0, 0), 1986: Squad(0, 16, 5, 22), 2014: Squad(2, 0, 0, 0)}
COSTA_RICA = {1990: Squad(0, 0, 0, 22), 2002: Squad(0, 3, 3, 23), 2006: Squad(0, 3, 1, 23),
              2014: Squad(1, 14, 11, 23)}
JAMAICA = {1998: Squad(0, 8, 7, 22)}

# Europe - UEFA
FRANCE = {1930: Squad(3, 0, 0, 16), 1934: Squad(1, 0, 0, 22), 1938: Squad(3, 0, 0, 22),
          1954: Squad(0, 0, 0, 22), 1958: Squad(0, 1, 0, 22), 1962: Squad(2, 0, 0, 0),
          1966: Squad(0, 2, 0, 22), 1974: Squad(3, 0, 0, 0), 1978: Squad(2, 0, 0, 22),
          1982: Squad(17, 0, 0, 22), 1986: Squad(16, 2, 0, 22), 1990: Squad(24, 0, 0, 0),
          1994: Squad(25, 0, 0, 0), 1998: Squad(20, 12, 0, 22), 2002: Squad(51, 18, 0, 23),
          2006: Squad(47, 12, 0, 23), 2010: Squad(32, 12, 0, 23), 2014: Squad(26, 15, 0, 23)}
ENGLAND = {1950: Squad(1, 0, 0, 22), 1954: Squad(7, 0, 0, 22), 1958: Squad(35, 0, 0, 22),
           1962: Squad(0, 1, 0, 22), 1966: Squad(0, 0, 0, 22), 1970: Squad(0, 0, 0, 22),
           1974: Squad(12, 0, 0, 0), 1978: Squad(15, 0, 0, 0), 1982: Squad(29, 0, 0, 22),
           1986: Squad(31, 0, 0, 22), 1990: Squad(29, 5, 0, 22), 1994: Squad(38, 0, 0, 0),
           1998: Squad(52, 0, 0, 22), 2002: Squad(81, 1, 0, 23), 2006: Squad(76, 2, 0, 23),
           2010: Squad(88, 0, 0, 23), 2014: Squad(65, 1, 0, 23)}
ITALY = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22),
         1954: Squad(0, 0, 0, 22), 1958: Squad(6, 0, 0, 0), 1962: Squad(4, 0, 0, 22),
         1966: Squad(7, 0, 0, 22), 1970: Squad(2, 0, 0, 22), 1974: Squad(0, 0, 0, 22),
         1978: Squad(0, 0, 0, 22), 1982: Squad(5, 0, 0, 22), 1986: Squad(16, 0, 0, 22),
         1990: Squad(31, 0, 0, 22), 1994: Squad(22, 0, 0, 22), 1998: Squad(50, 2, 0, 22),
         2002: Squad(53, 1, 0, 23), 2006: Squad(38, 0, 0, 23), 2010: Squad(56, 0, 0, 23),
         2014: Squad(49, 3, 0, 23)}
SPAIN = {1934: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22), 1958: Squad(1, 0, 0, 0),
         1962: Squad(0, 0, 0, 22), 1966: Squad(1, 3, 0, 22), 1974: Squad(7, 0, 0, 0),
         1978: Squad(2, 0, 0, 22), 1982: Squad(8, 0, 0, 22), 1986: Squad(6, 0, 0, 22),
         1990: Squad(13, 0, 0, 22), 1994: Squad(23, 0, 0, 22), 1998: Squad(48, 0, 0, 22),
         2002: Squad(36, 0, 0, 23), 2006: Squad(35, 18, 0, 23), 2010: Squad(40, 3, 0, 23),
         2014: Squad(36, 14, 0, 23)}
GERMANY = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
           1958: Squad(0, 0, 0, 22), 1962: Squad(0, 1, 0, 22), 1966: Squad(0, 3, 0, 22),
           1970: Squad(0, 2, 0, 22), 1974: Squad(3, 1, 0, 22), 1978: Squad(8, 0, 0, 22),
           1982: Squad(5, 1, 0, 22), 1986: Squad(2, 2, 0, 22), 1990: Squad(10, 5, 0, 22),
           1994: Squad(24, 6, 0, 22), 1998: Squad(35, 4, 0, 22), 2002: Squad(39, 3, 0, 23),
           2006: Squad(54, 2, 0, 23), 2010: Squad(62, 0, 0, 23), 2014: Squad(48, 0, 0, 0)}

TURKEY = {1954: Squad(0, 0, 0, 22), 1986: Squad(1, 0, 0, 0), 1994: Squad(2, 0, 0, 0),
          1998: Squad(18, 0, 0, 0), 2002: Squad(6, 10, 0, 23), 2006: Squad(12, 0, 0, 0),
          2010: Squad(14, 0, 0, 0), 2014: Squad(21, 0, 0, 0)}
SWITZERLAND = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 2, 0, 22), 1950: Squad(0, 0, 0, 22),
               1954: Squad(0, 0, 0, 22), 1962: Squad(0, 3, 0, 22), 1966: Squad(0, 0, 0, 22),
               1970: Squad(1, 0, 0, 0), 1974: Squad(1, 0, 0, 0), 1978: Squad(1, 0, 0, 0),
               1982: Squad(2, 0, 0, 0), 1986: Squad(4, 0, 0, 0), 1990: Squad(4, 0, 0, 0),
               1994: Squad(4, 4, 0, 22), 1998: Squad(5, 0, 0, 0), 2002: Squad(3, 0, 0, 0),
               2006: Squad(8, 17, 0, 23), 2010: Squad(3, 16, 0, 23), 2014: Squad(5, 16, 0, 23)}
GREECE = {1986: Squad(1, 0, 0, 0), 1990: Squad(1, 0, 0, 0), 1994: Squad(0, 0, 0, 22),
          1998: Squad(3, 0, 0, 0), 2002: Squad(10, 0, 0, 0), 2006: Squad(4, 0, 0, 0),
          2010: Squad(8, 14, 0, 23), 2014: Squad(2, 0, 0, 0), 2014: Squad(1, 14, 0, 23)}
NETHERLANDS = {1938: Squad(0, 0, 0, 22), 1970: Squad(1, 0, 0, 0), 1974: Squad(0, 3, 0, 22),
               1978: Squad(1, 6, 0, 22), 1986: Squad(6, 0, 0, 0), 1990: Squad(7, 8, 0, 22),
               1994: Squad(7, 8, 0, 22), 1998: Squad(13, 12, 0, 22), 2002: Squad(18, 0, 0, 0),
               2006: Squad(11, 9, 0, 23), 2010: Squad(24, 14, 0, 23), 2014: Squad(8, 13, 0, 23)}
BELGIUM = {1930: Squad(0, 0, 0, 16), 1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22),
           1954: Squad(0, 0, 0, 22), 1970: Squad(4, 0, 0, 22), 1974: Squad(2, 0, 0, 0),
           1978: Squad(6, 0, 0, 0), 1982: Squad(7, 2, 0, 22), 1986: Squad(6, 2, 0, 22),
           1990: Squad(4, 3, 0, 22), 1994: Squad(11, 2, 0, 22), 1998: Squad(2, 5, 0, 22),
           2002: Squad(10, 8, 0, 23), 2006: Squad(9, 0, 0, 0), 2010: Squad(8, 0, 0, 0),
           2014: Squad(8, 0, 0, 0)}
PORTUGAL = {1966: Squad(0, 0, 0, 22), 1974: Squad(1, 0, 0, 0), 1982: Squad(1, 0, 0, 0),
            1986: Squad(2, 0, 0, 22), 1990: Squad(9, 0, 0, 0), 1994: Squad(11, 0, 0, 0),
            1998: Squad(9, 0, 0, 0), 2002: Squad(5, 15, 0, 23), 2006: Squad(12, 15, 0, 23),
            2010: Squad(11, 13, 0, 23), 2014: Squad(11, 0, 0, 0)}
SCOTLAND = {1954: Squad(0, 7, 0, 22), 1958: Squad(2, 6, 0, 22), 1970: Squad(1, 0, 0, 0),
            1974: Squad(0, 12, 0, 22), 1978: Squad(0, 15, 0, 22), 1982: Squad(1, 13, 0, 22),
            1986: Squad(1, 9, 0, 22), 1990: Squad(7, 10, 0, 22), 1994: Squad(3, 0, 0, 0),
            1998: Squad(3, 10, 0, 22), 2002: Squad(7, 0, 0, 0), 2006: Squad(11, 0, 0, 0),
            2010: Squad(11, 0, 0, 0), 2014: Squad(4, 0, 0, 0)}
RUSSIA = {1994: Squad(0, 12, 0, 22), 1998: Squad(1, 0, 0, 0), 2002: Squad(3, 9, 0, 23),
          2006: Squad(10, 0, 0, 0), 2010: Squad(14, 0, 0, 23), 2014: Squad(6, 0, 0, 0)}

YUGOSLAVIA = {1930: Squad(0, 3, 0, 17), 1950: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
              1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1974: Squad(0, 1, 0, 22),
              1982: Squad(0, 6, 0, 22), 1990: Squad(0, 9, 0, 22), 1998: Squad(0, 19, 2, 22),
              2002: Squad(1, 0, 0, 0)}
ROMANIA = {1930: Squad(0, 0, 0, 15), 1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22),
           1970: Squad(0, 0, 0, 22), 1990: Squad(0, 1, 0, 22), 1994: Squad(0, 7, 0, 22),
           1998: Squad(0, 16, 1, 22), 2010: Squad(4, 0, 0, 0), 2014: Squad(1, 0, 0, 0)}
AUSTRIA = {1934: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22), 1958: Squad(0, 0, 0, 22),
           1978: Squad(0, 5, 0, 22), 1982: Squad(1, 6, 0, 22), 1990: Squad(0, 1, 0, 22),
           1998: Squad(0, 17, 17, 22), 1998: Squad(3, 10, 0, 22), 2002: Squad(3, 0, 0, 0),
           2006: Squad(7, 0, 0, 0), 2010: Squad(1, 0, 0, 0), 2014: Squad(1, 0, 0, 0)}
CZECHOSLOVAKIA = {1934: Squad(0, 1, 0, 22), 1938: Squad(0, 0, 0, 22), 1954: Squad(0, 0, 0, 22),
                  1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1970: Squad(0, 1, 0, 22),
                  1982: Squad(0, 1, 0, 22), 1990: Squad(0, 8, 0, 22)}
EAST_GERMANY = {1974: Squad(0, 0, 0, 22)}
HUNGARY = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 1, 0, 22), 1954: Squad(0, 0, 0, 22),
           1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
           1978: Squad(0, 0, 0, 22), 1982: Squad(0, 5, 0, 22), 1986: Squad(0, 3, 0, 22),
           1990: Squad(1, 0, 0, 0), 1994: Squad(1, 0, 0, 0), 2014: Squad(1, 0, 0, 0)}

SWEDEN = {1934: Squad(0, 0, 0, 22), 1938: Squad(0, 0, 0, 22), 1950: Squad(0, 0, 0, 22),
          1958: Squad(0, 5, 0, 22), 1970: Squad(0, 6, 0, 22), 1974: Squad(0, 6, 0, 22),
          1978: Squad(0, 6, 0, 22), 1990: Squad(0, 11, 0, 22), 1994: Squad(0, 12, 0, 22),
          2002: Squad(1, 0, 0, 0), 2002: Squad(0, 20, 0, 23), 2006: Squad(2, 17, 0, 23),
          2010: Squad(1, 0, 0, 0), 2014: Squad(2, 0, 0, 0)}

POLAND = {1938: Squad(0, 0, 0, 22), 1974: Squad(0, 0, 0, 22), 1978: Squad(0, 1, 0, 22),
          1986: Squad(0, 4, 0, 22), 2002: Squad(0, 15, 0, 23), 2006: Squad(0, 8, 1, 23),
          2010: Squad(3, 0, 0, 0)}
NORWAY = {1938: Squad(0, 0, 0, 22), 1982: Squad(0, 2, 0, 22), 1994: Squad(0, 15, 0, 22),
          2002: Squad(1, 0, 0, 0), 2006: Squad(2, 0, 0, 0), 2010: Squad(2, 0, 0, 0),
          2014: Squad(3, 0, 0, 0)}

NORTHERN_IRELAND = {1958: Squad(0, 19, 0, 22), 1982: Squad(0, 18, 2, 22),
                    1986: Squad(0, 20, 0, 22)}
WALES = {1958: Squad(0, 13, 0, 22), 2006: Squad(1, 0, 0, 0), 2014: Squad(4, 0, 0, 0)}
SOVIET_UNION = {1958: Squad(0, 0, 0, 22), 1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22),
                1970: Squad(0, 0, 0, 22), 1982: Squad(0, 0, 0, 22), 1986: Squad(0, 0, 0, 22),
                1990: Squad(0, 7, 0, 22)}
BULGARIA = {1962: Squad(0, 0, 0, 22), 1966: Squad(0, 0, 0, 22), 1970: Squad(0, 0, 0, 22),
            1974: Squad(0, 0, 0, 22), 1986: Squad(0, 2, 0, 22), 1994: Squad(0, 13, 0, 22),
            1998: Squad(0, 10, 0, 22), 2002: Squad(1, 0, 0, 0), 2006: Squad(1, 0, 0, 0),
            2010: Squad(1, 0, 0, 0)}
ISRAEL = {1970: Squad(0, 0, 0, 22), 2002: Squad(2, 0, 0, 0), 2006: Squad(3, 0, 0, 0),
          2010: Squad(1, 0, 0, 0), 2010: Squad(5, 0, 0, 0), 2014: Squad(2, 0, 0, 0)}
DENMARK = {1986: Squad(0, 15, 0, 22), 1994: Squad(2, 0, 0, 0), 1998: Squad(1, 16, 0, 22),
           2002: Squad(1, 20, 0, 23), 2002: Squad(4, 0, 0, 0), 2006: Squad(6, 0, 0, 0),
           2010: Squad(2, 16, 0, 23), 2014: Squad(1, 0, 0, 0)}

IRELAND = {1990: Squad(0, 22, 0, 22), 1994: Squad(0, 22, 0, 22), 2002: Squad(0, 23, 0, 23)}
CROATIA = {1998: Squad(0, 12, 0, 22), 2002: Squad(0, 19, 0, 23), 2006: Squad(0, 20, 20, 23),
           2014: Squad(2, 21, 0, 23)}
SLOVENIA = {2002: Squad(0, 18, 1, 23), 2010: Squad(0, 21, 0, 23)}
UKRAINE = {2002: Squad(2, 0, 0, 0), 2006: Squad(8, 4, 0, 23), 2010: Squad(2, 0, 0, 0),
           2014: Squad(8, 0, 0, 0)}
SERBIA = {2006: Squad(1, 16, 0, 23), 2010: Squad(0, 21, 0, 23)}
CZECH_REPUBLIC = {2002: Squad(1, 0, 0, 0), 2006: Squad(1, 21, 0, 23), 2010: Squad(1, 0, 0, 0)}
CYPRUS = {2006: Squad(1, 0, 0, 0), 2010: Squad(1, 0, 0, 0)}
SLOVAKIA = {2010: Squad(0, 21, 0, 23)}
BOSNIA = {2014: Squad(0, 22, 1, 23)}

# Africa -
EGYPT = {1934: Squad(0, 0, 0, 20), 1990: Squad(0, 2, 2, 22), 1994: Squad(1, 0, 0, 0),
         2006: Squad(1, 0, 0, 0), 2010: Squad(1, 0, 0, 0)}
MOROCCO = {1970: Squad(0, 0, 0, 19), 1986: Squad(0, 5, 5, 22), 1994: Squad(0, 9, 0, 22),
           1998: Squad(0, 16, 15, 22), 2002: Squad(1, 0, 0, 0)}
ZAIRE = {1974: Squad(0, 0, 0, 22)}
TUNISIA = {1978: Squad(0, 2, 2, 22), 1998: Squad(1, 4, 4, 22), 2002: Squad(0, 9, 9, 23),
           2006: Squad(0, 19, 19, 23)}
CAMEROON = {1982: Squad(0, 6, 5, 22), 1990: Squad(0, 11, 11, 22), 1994: Squad(0, 11, 11, 22),
            1998: Squad(0, 18, 18, 22), 2002: Squad(0, 23, 23, 23), 2010: Squad(0, 22, 22, 23),
            2014: Squad(0, 21, 21, 23)}
ALGERIA = {1982: Squad(0, 7, 7, 22), 1986: Squad(0, 11, 11, 22), 2010: Squad(0, 20, 20, 23)}
IVORY_COAST = {1982: Squad(1, 0, 0, 0), 1994: Squad(1, 0, 0, 0), 2006: Squad(0, 23, 22, 23),
               2010: Squad(0, 22, 22, 23), 2014: Squad(0, 22, 22, 23)}
NIGERIA = {1994: Squad(0, 22, 20, 22), 1998: Squad(0, 22, 21, 22), 2002: Squad(0, 20, 20, 23),
           2010: Squad(0, 23, 23, 23), 2014: Squad(0, 19, 19, 23)}
SENEGAL = {2002: Squad(0, 22, 21, 23)}
ANGOLA = {2006: Squad(0, 14, 13, 23)}
GHANA = {2006: Squad(0, 19, 19, 23), 2010: Squad(0, 20, 19, 23)}
TOGO = {2006: Squad(0, 22, 21, 23)}
MALI = {2006: Squad(1, 0, 0, 0)}
SOUTH_AFRICA = {1998: Squad(1, 14, 14, 22), 2002: Squad(0, 16, 16, 23), 2010: Squad(0, 7, 7, 23)}

# Asia & Oceania -
DUTCH_EAST_INDIES = {1938: Squad(0, 0, 0, 17)}
SOUTH_KOREA = {1954: Squad(0, 0, 0, 20), 1986: Squad(0, 1, 1, 22), 1990: Squad(0, 0, 0, 22),
               1994: Squad(0, 2, 1, 22), 1998: Squad(1, 5, 2, 22), 2002: Squad(0, 7, 2, 23),
               2006: Squad(0, 7, 5, 23), 2010: Squad(0, 10, 7, 23), 2014: Squad(1, 0, 0, 0)}
NORTH_KOREA = {1966: Squad(0, 0, 0, 22), 2010: Squad(0, 3, 1, 23)}
AUSTRALIA = {1974: Squad(0, 0, 0, 22), 2006: Squad(1, 20, 20, 23), 2010: Squad(12, 20, 18, 23),
             2014: Squad(0, 16, 14, 23)}
IRAN = {1978: Squad(0, 0, 0, 22), 1998: Squad(0, 3, 3, 22), 2006: Squad(0, 16, 15, 23),
        2014: Squad(0, 9, 7, 23)}
SAUDI_ARABIA = {1978: Squad(1, 0, 0, 0), 1994: Squad(1, 0, 0, 22), 1998: Squad(0, 0, 0, 22),
                2002: Squad(1, 0, 0, 23), 2006: Squad(1, 0, 0, 23), 2010: Squad(1, 0, 0, 0)}
KUWAIT = {1982: Squad(0, 0, 0, 22), 2014: Squad(1, 0, 0, 0)}
NEW_ZEALAND = {1982: Squad(0, 0, 0, 22), 2010: Squad(0, 21, 9, 23)}
IRAQ = {1986: Squad(0, 0, 0, 22)}
UAE = {1990: Squad(0, 0, 0, 22), 2006: Squad(2, 0, 0, 0), 2010: Squad(2, 0, 0, 0),
       2014: Squad(1, 0, 0, 0)}
JAPAN = {1994: Squad(3, 0, 0, 0), 1998: Squad(8, 0, 0, 22), 2002: Squad(6, 4, 4, 23),
         2006: Squad(2, 17, 17, 23), 2010: Squad(6, 4, 4, 23), 2014: Squad(1, 12, 12, 23)}
QATAR = {1994: Squad(1, 0, 0, 0), 2002: Squad(1, 0, 0, 0), 2006: Squad(4, 0, 0, 0),
         2010: Squad(1, 0, 0, 0), 2014: Squad(2, 0, 0, 0)}
CHINA = {1998: Squad(1, 0, 0, 0), 2002: Squad(1, 3, 3, 23), 2010: Squad(3, 0, 0, 0),
         2014: Squad(3, 0, 0, 0)}
