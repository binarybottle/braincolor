
import networkx as nx

G = nx.Graph()

G.add_node("FRP",   id="111", lobe="FL", sub="lateral surface")
G.add_node("SFG",   id="112", lobe="FL", sub="lateral surface")
G.add_node("MFG",   id="113", lobe="FL", sub="lateral surface")
G.add_node("OpIFG", id="114", lobe="FL", sub="lateral surface")
G.add_node("OrIFG", id="115", lobe="FL", sub="lateral surface")
G.add_node("TrIFG", id="116", lobe="FL", sub="lateral surface")
G.add_node("PrG",   id="117", lobe="FL", sub="lateral surface")
           
G.add_node("MSFG",  id="121", lobe="FL", sub="medial surface")
G.add_node("SMC",   id="122", lobe="FL", sub="medial surface")
G.add_node("MFC",   id="123", lobe="FL", sub="medial surface")
G.add_node("GRe",   id="124", lobe="FL", sub="medial surface")
G.add_node("SCA",   id="125", lobe="FL", sub="medial surface")
G.add_node("MPrG",  id="126", lobe="FL", sub="medial surface")
           
G.add_node("AOrG",  id="131", lobe="FL", sub="inferior surface")
G.add_node("MOrG",  id="132", lobe="FL", sub="inferior surface")
G.add_node("LOrG",  id="133", lobe="FL", sub="inferior surface")
G.add_node("POrG",  id="134", lobe="FL", sub="inferior surface")
           
G.add_node("FO",    id="141", lobe="FL", sub="opercular region")
G.add_node("CO",    id="142", lobe="FL", sub="opercular region")
G.add_node("PO",    id="143", lobe="FL", sub="opercular region")
           
G.add_node("AIns",  id="151", lobe="FL", sub="insular region")
G.add_node("PIns",  id="152", lobe="FL", sub="insular region")
           
           
G.add_node("TMP",   id="211", lobe="TL", sub="lateral surface")
G.add_node("STG",   id="212", lobe="TL", sub="lateral surface")
G.add_node("MTG",   id="213", lobe="TL", sub="lateral surface")
G.add_node("ITG",   id="214", lobe="TL", sub="lateral surface")
           
G.add_node("PP",    id="221", lobe="TL", sub="supratemporal surface")
G.add_node("TTG",   id="222", lobe="TL", sub="supratemporal surface")
G.add_node("PT",    id="223", lobe="TL", sub="supratemporal surface")
           
G.add_node("FuG",   id="231", lobe="TL", sub="inferior surface")
           
           
G.add_node("PoG",   id="311", lobe="PL", sub="lateral surface")
G.add_node("SMG",   id="312", lobe="PL", sub="lateral surface")
G.add_node("SPL",   id="313", lobe="PL", sub="lateral surface")
G.add_node("AnG",   id="314", lobe="PL", sub="lateral surface")
           
G.add_node("MPoG",  id="321", lobe="PL", sub="medial surface")
G.add_node("PCu",   id="322", lobe="PL", sub="medial surface")
           
           
G.add_node("SOG",   id="411", lobe="OL", sub="lateral surface")
G.add_node("IOG",   id="412", lobe="OL", sub="lateral surface")
G.add_node("MOG",   id="413", lobe="OL", sub="lateral surface")
G.add_node("OCP",   id="414", lobe="OL", sub="lateral surface")
           
G.add_node("OFuG",  id="421", lobe="OL", sub="inferior surface")
           
G.add_node("Cun",   id="431", lobe="OL", sub="medial surface")
G.add_node("Calc",  id="432", lobe="OL", sub="medial surface")
G.add_node("LiG",   id="433", lobe="OL", sub="medial surface")
           
           
G.add_node("ACgG",  id="511", lobe="LC", sub="cingulate cortex")
G.add_node("MCgG",  id="512", lobe="LC", sub="cingulate cortex")
G.add_node("PCgG",  id="513", lobe="LC", sub="cingulate cortex")
           
G.add_node("PHG",   id="521", lobe="LC", sub="medial temporal cortex")
G.add_node("Ent",   id="522", lobe="LC", sub="medial temporal cortex")


G.add_edge("FRP","SFG")
G.add_edge("FRP","MFG")
G.add_edge("SFG","MFG")
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
