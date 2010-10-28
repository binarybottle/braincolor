
import networkx as nx

G = nx.Graph()
                             
G.add_node("111", roi="FRP",   lobe="FL", sub="lateral surface")
G.add_node("112", roi="SFG",   lobe="FL", sub="lateral surface")
G.add_node("113", roi="MFG",   lobe="FL", sub="lateral surface")
G.add_node("114", roi="OpIFG", lobe="FL", sub="lateral surface")
G.add_node("115", roi="ORIFG", lobe="FL", sub="lateral surface")
G.add_node("116", roi="TrIFG", lobe="FL", sub="lateral surface")
G.add_node("117", roi="PrG",   lobe="FL", sub="lateral surface")

G.add_node("121", roi="MSFG",  lobe="FL", sub="medial surface")
G.add_node("122", roi="SMC",   lobe="FL", sub="medial surface")
G.add_node("123", roi="MFC",   lobe="FL", sub="medial surface")
G.add_node("124", roi="GRe",   lobe="FL", sub="medial surface")
G.add_node("125", roi="SCA",   lobe="FL", sub="medial surface")
G.add_node("126", roi="MPrG",  lobe="FL", sub="medial surface")

G.add_node("131", roi="AOrG",  lobe="FL", sub="inferior surface")
G.add_node("132", roi="MOrG",  lobe="FL", sub="inferior surface")
G.add_node("133", roi="LOrG",  lobe="FL", sub="inferior surface")
G.add_node("134", roi="POrG",  lobe="FL", sub="inferior surface")

G.add_node("141", roi="FO",    lobe="FL", sub="opercular region")
G.add_node("142", roi="CO",    lobe="FL", sub="opercular region")
G.add_node("143", roi="PO",    lobe="FL", sub="opercular region")

G.add_node("151", roi="AIns",  lobe="FL", sub="insular region")
G.add_node("152", roi="PIns",  lobe="FL", sub="insular region")


G.add_node("211", roi="TMP",   lobe="TL", sub="lateral surface")
G.add_node("212", roi="STG",   lobe="TL", sub="lateral surface")
G.add_node("213", roi="MTG",   lobe="TL", sub="lateral surface")
G.add_node("214", roi="ITG",   lobe="TL", sub="lateral surface")

G.add_node("221", roi="PP",    lobe="TL", sub="supratemporal surface")
G.add_node("222", roi="TTG",   lobe="TL", sub="supratemporal surface")
G.add_node("223", roi="PT",    lobe="TL", sub="supratemporal surface")

G.add_node("231", roi="FuG",   lobe="TL", sub="inferior surface")


G.add_node("311", roi="PoG",   lobe="PL", sub="lateral surface")
G.add_node("312", roi="SMG",   lobe="PL", sub="lateral surface")
G.add_node("313", roi="SPL",   lobe="PL", sub="lateral surface")
G.add_node("314", roi="AnG",   lobe="PL", sub="lateral surface")

G.add_node("321", roi="MPoG",  lobe="PL", sub="medial surface")
G.add_node("322", roi="PCu",   lobe="PL", sub="medial surface")


G.add_node("411", roi="SOG",   lobe="OL", sub="lateral surface")
G.add_node("412", roi="IOG",   lobe="OL", sub="lateral surface")
G.add_node("413", roi="MOG",   lobe="OL", sub="lateral surface")
G.add_node("414", roi="OCP",   lobe="OL", sub="lateral surface")

G.add_node("421", roi="OFuG",  lobe="OL", sub="inferior surface")

G.add_node("431", roi="Cun",   lobe="OL", sub="medial surface")
G.add_node("432", roi="Calc",  lobe="OL", sub="medial surface")
G.add_node("433", roi="LiG",   lobe="OL", sub="medial surface")


G.add_node("511", roi="ACgG",  lobe="LC", sub="cingulate cortex")
G.add_node("512", roi="MCgG",  lobe="LC", sub="cingulate cortex")
G.add_node("513", roi="PCgG",  lobe="LC", sub="cingulate cortex")

G.add_node("521", roi="PHG",   lobe="LC", sub="medial temporal cortex")
G.add_node("522", roi="Ent",   lobe="LC", sub="medial temporal cortex")


G.add_edge("111","112")
G.add_edge("111","113")
G.add_edge("111","115")
G.add_edge("117","126")
G.add_edge("126","122")
G.add_edge("117","112")
G.add_edge("117","113")
G.add_edge("117","114")
G.add_edge("122","121")
G.add_edge("121","123")
G.add_edge("123","124")
G.add_edge("123","125")
G.add_edge("152","152")

"""
G.add_edge("TMP","STG")
G.add_edge("TMP","MTG")
G.add_edge("TMP","ITG")
G.add_edge("STG","MTG")
G.add_edge("MTG","ITG")
G.add_edge("ITG","FuG")


G.add_edge("PoG","SPG")
G.add_edge("PoG","SMG")
G.add_edge("SPL","SMG")
G.add_edge("SPL","AnG")
G.add_edge("SMG","AnG")
G.add_edge("MPoG","PCu")


G.add_edge("OCP","SOG")
G.add_edge("OCP","MOG")
G.add_edge("OCP","IOG")
G.add_edge("SOG","MOG")
G.add_edge("SOG","IOG")
G.add_edge("MOG","IOG")
G.add_edge("OFuG","LiG")


G.add_edge("ACgG","MCgG")
G.add_edge("MCgG","PCgG")
G.add_edge("PHG","Ent")
"""