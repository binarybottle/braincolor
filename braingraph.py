
import networkx as nx

G = nx.Graph()

G.add_node("FRP",   num="111", lobe="FL", sub="lateral surface")
G.add_node("SFG",   num="112", lobe="FL", sub="lateral surface")
G.add_node("MFG",   num="113", lobe="FL", sub="lateral surface")
G.add_node("OpIFG", num="114", lobe="FL", sub="lateral surface")
G.add_node("OrIFG", num="115", lobe="FL", sub="lateral surface")
G.add_node("TrIFG", num="116", lobe="FL", sub="lateral surface")
G.add_node("PrG",   num="117", lobe="FL", sub="lateral surface")
           
G.add_node("MSFG",  num="121", lobe="FL", sub="medial surface")
G.add_node("SMC",   num="122", lobe="FL", sub="medial surface")
G.add_node("MFC",   num="123", lobe="FL", sub="medial surface")
G.add_node("GRe",   num="124", lobe="FL", sub="medial surface")
G.add_node("SCA",   num="125", lobe="FL", sub="medial surface")
G.add_node("MPrG",  num="126", lobe="FL", sub="medial surface")
           
G.add_node("AOrG",  num="131", lobe="FL", sub="inferior surface")
G.add_node("MOrG",  num="132", lobe="FL", sub="inferior surface")
G.add_node("LOrG",  num="133", lobe="FL", sub="inferior surface")
G.add_node("POrG",  num="134", lobe="FL", sub="inferior surface")
           
G.add_node("FO",    num="141", lobe="FL", sub="opercular region")
G.add_node("CO",    num="142", lobe="FL", sub="opercular region")
G.add_node("PO",    num="143", lobe="FL", sub="opercular region")
           
G.add_node("AIns",  num="151", lobe="FL", sub="insular region")
G.add_node("PIns",  num="152", lobe="FL", sub="insular region")
           
           
G.add_node("TMP",   num="211", lobe="TL", sub="lateral surface")
G.add_node("STG",   num="212", lobe="TL", sub="lateral surface")
G.add_node("MTG",   num="213", lobe="TL", sub="lateral surface")
G.add_node("ITG",   num="214", lobe="TL", sub="lateral surface")
           
G.add_node("PP",    num="221", lobe="TL", sub="supratemporal surface")
G.add_node("TTG",   num="222", lobe="TL", sub="supratemporal surface")
G.add_node("PT",    num="223", lobe="TL", sub="supratemporal surface")
           
G.add_node("FuG",   num="231", lobe="TL", sub="inferior surface")
           
           
G.add_node("PoG",   num="311", lobe="PL", sub="lateral surface")
G.add_node("SMG",   num="312", lobe="PL", sub="lateral surface")
G.add_node("SPL",   num="313", lobe="PL", sub="lateral surface")
G.add_node("AnG",   num="314", lobe="PL", sub="lateral surface")
           
G.add_node("MPoG",  num="321", lobe="PL", sub="medial surface")
G.add_node("PCu",   num="322", lobe="PL", sub="medial surface")
           
           
G.add_node("SOG",   num="411", lobe="OL", sub="lateral surface")
G.add_node("IOG",   num="412", lobe="OL", sub="lateral surface")
G.add_node("MOG",   num="413", lobe="OL", sub="lateral surface")
G.add_node("OCP",   num="414", lobe="OL", sub="lateral surface")
           
G.add_node("OFuG",  num="421", lobe="OL", sub="inferior surface")
           
G.add_node("Cun",   num="431", lobe="OL", sub="medial surface")
G.add_node("Calc",  num="432", lobe="OL", sub="medial surface")
G.add_node("LiG",   num="433", lobe="OL", sub="medial surface")
           
           
G.add_node("ACgG",  num="511", lobe="LC", sub="cingulate cortex")
G.add_node("MCgG",  num="512", lobe="LC", sub="cingulate cortex")
G.add_node("PCgG",  num="513", lobe="LC", sub="cingulate cortex")
           
G.add_node("PHG",   num="521", lobe="LC", sub="medial temporal cortex")
G.add_node("Ent",   num="522", lobe="LC", sub="medial temporal cortex")


G.add_edge("FRP","SFG")
G.add_edge("FRP","MFG")
G.add_edge("FRP","OrIFG")
G.add_edge("PrG","MPrG")
G.add_edge("MPrG","SMC")
G.add_edge("PrG","SFG")
G.add_edge("PrG","MFG")
G.add_edge("PrG","OpIFG")
#G.add_edge("OrIPG","OFC")
G.add_edge("SMC","MSFG")
G.add_edge("MSFG","MFC")
G.add_edge("MFC","GRe")
G.add_edge("MFC","SCA")
G.add_edge("AIns","PIns")


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
