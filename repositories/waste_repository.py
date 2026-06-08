"""Waste Repository – A-to-Z waste item dataset."""

from models.waste_item import WasteItem
from models.waste_category import WasteCategory
from models.disposal_guide import DisposalGuide


class WasteRepository:
    def __init__(self):
        self._items: dict[str, WasteItem] = {}
        self._load_data()

    # ── Data ────────────────────────────────────────────────────────────────
    def _load_data(self):
        items = [
            # ── A ──
            WasteItem("Aerosol Can", WasteCategory.HAZARDOUS,
                DisposalGuide(
                    "Empty completely, then recycle the metal can",
                    ["Shake to confirm empty before disposal", "Remove plastic cap and recycle separately"],
                    ["Never puncture or incinerate", "Do not dispose of full cans in trash"])),
            WasteItem("Aluminum Foil", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Clean and ball up before placing in recycling bin",
                    ["Rinse off food residue", "Ball multiple pieces together so they don't blow away"],
                    ["Heavily soiled foil should go in general waste"])),
            WasteItem("Apple Core", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Place in compost bin or green waste bin",
                    ["Great nitrogen source for compost", "Can also be buried directly in garden soil"],
                    [])),

            # ── B ──
            WasteItem("Banana Peel", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Add to compost bin or green waste collection",
                    ["Rich in potassium – excellent for soil", "Break into smaller pieces to speed composting"],
                    ["Avoid adding peels from heavily waxed or sprayed fruit to food compost"])),
            WasteItem("Battery (AA/AAA)", WasteCategory.HAZARDOUS,
                DisposalGuide(
                    "Drop off at a designated battery recycling point (supermarket, hardware store)",
                    ["Store spent batteries in a sealed container until drop-off", "Many retailers offer free collection"],
                    ["Never throw in household trash – contains heavy metals", "Do not expose to heat or puncture"])),
            WasteItem("Bubble Wrap", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Check for a plastic film drop-off bin at major supermarkets",
                    ["Reuse for packing before recycling", "Deflate bubbles to save space"],
                    ["Not accepted in kerbside recycling bins"])),

            # ── C ──
            WasteItem("Cardboard Box", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Flatten and place in paper/cardboard recycling bin",
                    ["Remove all tape and staples first", "Keep dry – wet cardboard is not recyclable"],
                    ["Pizza boxes with heavy grease stains go in general waste"])),
            WasteItem("Car Oil (Used)", WasteCategory.HAZARDOUS,
                DisposalGuide(
                    "Take to an automotive shop or hazardous waste facility for recycling",
                    ["Store in original sealed container", "Many service stations accept used oil for free"],
                    ["Never pour down drains – contaminates water supply", "Do not mix with other liquids"])),
            WasteItem("Cereal Box", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Remove inner plastic liner, flatten, and recycle with cardboard",
                    ["The inner bag is usually not recyclable – check for film plastic drop-off"],
                    [])),
            WasteItem("Coffee Grounds", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Add to compost bin or sprinkle directly in garden",
                    ["Great for acid-loving plants like blueberries", "Mix with brown material in compost"],
                    ["Avoid using in large amounts around pets"])),
            WasteItem("Computer (Old)", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Take to an e-waste recycling centre or retailer take-back programme",
                    ["Wipe your hard drive before disposal", "Donate if still functional"],
                    ["Never place in general waste – contains toxic components"])),

            # ── D ──
            WasteItem("Dead Batteries (Lithium)", WasteCategory.HAZARDOUS,
                DisposalGuide(
                    "Take to a specialist lithium battery recycling point",
                    ["Tape the terminals before storage/transport", "Many electronics shops accept these"],
                    ["Risk of fire if punctured or improperly stored", "Never put in household recycling"])),
            WasteItem("Diapers (Used)", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Wrap securely and place in general household waste bin",
                    ["Use a sealed nappy bag to reduce odour", "Some councils offer specialist nappy disposal schemes"],
                    ["Do not flush – causes blockages", "Not suitable for recycling or composting"])),
            WasteItem("Drinking Glass (Broken)", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Wrap in newspaper or thick paper, tape shut, and place in general waste",
                    ["Label the package 'sharp glass' for safety", "Do not place loose in recycling – different composition from bottle glass"],
                    ["Never put loose broken glass in a bin bag unprotected"])),

            # ── E ──
            WasteItem("Egg Carton (Paper)", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Place in paper/cardboard recycling bin",
                    ["Great for starting seedlings before composting the whole tray", "Can be composted if soiled"],
                    [])),
            WasteItem("Egg Shells", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Add to compost bin or crush and sprinkle on garden soil",
                    ["Rich in calcium – great for soil pH balance", "Crush before composting to speed breakdown"],
                    [])),
            WasteItem("Electronic Cables", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Drop off at an e-waste collection point or retailer take-back bin",
                    ["Bundle cables together to keep organised for drop-off", "Some charities accept working cables"],
                    ["Do not place in household recycling or general waste"])),

            # ── F ──
            WasteItem("Fluorescent Light Bulb", WasteCategory.HAZARDOUS,
                DisposalGuide(
                    "Take to a household hazardous waste facility or bulb recycling drop-off",
                    ["Many hardware stores accept old fluorescent bulbs", "Keep in original packaging if possible"],
                    ["Contains mercury – never break or put in general waste"])),
            WasteItem("Food Scraps (Mixed)", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Place in food waste caddy or compost bin",
                    ["Include fruit and vegetable peelings, tea bags, and coffee grounds", "Use compostable liners in your caddy"],
                    ["Avoid adding meat or fish to home compost – use council food waste collection instead"])),
            WasteItem("Foam Packaging (Styrofoam)", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Check local authority – some accept it at recycling centres",
                    ["Reuse for packing material where possible", "Some specialist mail-in recyclers accept EPS foam"],
                    ["Not accepted in most kerbside recycling", "Do not burn – releases toxic gases"])),

            # ── G ──
            WasteItem("Garden Waste (Leaves/Grass)", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Place in green waste bin or home compost heap",
                    ["Autumn leaves make excellent leaf mould after 1–2 years", "Mix green and brown material in compost"],
                    ["Do not include diseased plants"])),
            WasteItem("Glass Bottle", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Rinse and place in glass recycling bin",
                    ["Remove corks and metal caps (recycle metal caps separately)", "No need to remove labels"],
                    ["Do not mix with ceramics or Pyrex – different melting points"])),
            WasteItem("Glass Jar", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Rinse and place in glass recycling bin or bottle bank",
                    ["Remove metal lids – recycle separately with metals", "No need to remove paper labels"],
                    ["Check local rules – some councils only accept certain glass colours"])),

            # ── H ──
            WasteItem("Hair (Human/Pet)", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Add small amounts to compost bin",
                    ["Rich in nitrogen – good activator for compost", "Stuff in a mesh bag and hang in garden to deter deer"],
                    [])),
            WasteItem("Hardware (Nails/Screws)", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Collect in a metal container and take to a scrap metal dealer or recycling centre",
                    ["Keep metals sorted by type where possible", "Some charities accept reusable hardware"],
                    ["Never place loose sharp metal in a bin bag"])),

            # ── I ──
            WasteItem("Ink Cartridge", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Return to manufacturer, office supply retailer, or e-waste drop-off",
                    ["Many brands offer free postage for empty cartridges", "Some supermarkets have collection boxes"],
                    ["Do not dispose in general waste – contains residual ink and plastic"])),

            # ── J ──
            WasteItem("Junk Mail (Paper)", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Place in paper recycling bin",
                    ["Shred documents with personal information before recycling", "Remove plastic windows from envelopes"],
                    [])),

            # ── K ──
            WasteItem("Kitchen Roll (Used)", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Add to compost bin or general waste if soiled with chemicals",
                    ["Plain paper towels with food waste are compostable", "The cardboard tube can be recycled"],
                    ["Do not recycle if used to clean up chemicals or grease"])),

            # ── L ──
            WasteItem("Laptop", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Take to an approved e-waste recycling centre or retailer take-back scheme",
                    ["Back up and wipe data before disposal", "Check manufacturer for trade-in or recycling programmes"],
                    ["Contains lithium battery – never dispose of in general waste or fire"])),
            WasteItem("Light Bulb (LED)", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Take to a retailer or council recycling drop-off point",
                    ["Many hardware and lighting stores collect old LEDs", "Handle with care to avoid breaking"],
                    ["Do not place in general recycling bin"])),

            # ── M ──
            WasteItem("Magazine", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Place in paper recycling bin",
                    ["Donate to waiting rooms, libraries, or community centres if still in good condition", "Remove free plastic gifts or discs before recycling"],
                    [])),
            WasteItem("Medicine (Expired)", WasteCategory.MEDICAL,
                DisposalGuide(
                    "Return to a pharmacy for safe disposal",
                    ["Never flush medication down the toilet", "Many pharmacies accept all forms of medication"],
                    ["Do not place in household waste – risk of contamination", "Keep out of reach of children until disposed of"])),
            WasteItem("Metal Cans (Food/Drink)", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Rinse and place in metal/mixed recycling bin",
                    ["Crush to save space", "Leave the lid inside the can after cutting"],
                    [])),
            WasteItem("Mobile Phone (Old)", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Donate, sell, or take to an e-waste collection point",
                    ["Factory reset and remove SIM/memory card first", "Many charities accept old phones"],
                    ["Contains lithium battery – never dispose of in general waste"])),

            # ── N ──
            WasteItem("Newspaper", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Place in paper recycling bin",
                    ["Great as packaging material or pet cage lining before recycling", "Keep dry"],
                    [])),

            # ── O ──
            WasteItem("Olive Oil (Cooking)", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Let cool and solidify, then dispose in general waste or compost in small amounts",
                    ["Small amounts can be poured into compost", "Local authority cooking oil recycling points accept larger quantities"],
                    ["Never pour large amounts down the sink – causes drain blockages"])),

            # ── P ──
            WasteItem("Paint (Leftover)", WasteCategory.HAZARDOUS,
                DisposalGuide(
                    "Take to a household hazardous waste facility or community repaint scheme",
                    ["Community RePaint accepts usable paint for redistribution", "Let small amounts dry out before disposing in general waste"],
                    ["Never pour liquid paint down the drain", "Do not mix different paint types"])),
            WasteItem("Plastic Bag", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Return to supermarket plastic film recycling bin",
                    ["Reuse as many times as possible before recycling", "Scrunch test: if it scrunches into a ball, it's film plastic"],
                    ["Not accepted in kerbside recycling – clogs machinery"])),
            WasteItem("Plastic Bottle", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Rinse, replace cap, and place in plastic recycling bin",
                    ["Crush to save space", "Remove pumps from soap/shampoo bottles"],
                    ["Check for recycling number on base – #1 and #2 are most widely accepted"])),
            WasteItem("Printer Paper", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Place in paper recycling bin",
                    ["Both sides can be used before recycling", "Shred documents with personal info first"],
                    [])),

            # ── R ──
            WasteItem("Rubber Tyres", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Take to a tyre retailer or council recycling centre – they must be accepted by law",
                    ["Some centres charge a small fee", "Tyres can be repurposed as garden planters or playground equipment"],
                    ["Never dump illegally – heavy fines apply", "Do not burn – releases toxic black smoke"])),

            # ── S ──
            WasteItem("Shampoo Bottle", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Rinse empty bottle and recycle with plastics",
                    ["Remove pump dispenser (check if recyclable separately)", "Squeeze out remaining product or rinse"],
                    [])),
            WasteItem("Smartphone", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Sell, donate, or take to an e-waste collection point",
                    ["Factory reset and remove SIM card and accounts", "Many manufacturers and carriers offer trade-in programmes"],
                    ["Contains lithium battery and rare metals – never in general waste"])),
            WasteItem("Soiled Paper Towels", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Compost if soiled only with food; general waste if contaminated with chemicals",
                    ["Food-soiled paper towels are compostable in council food waste collections", "Use as 'brown material' in compost heap"],
                    ["Do not recycle soiled paper"])),
            WasteItem("Syringes (Medical)", WasteCategory.MEDICAL,
                DisposalGuide(
                    "Place in a sharps container and return to a pharmacy or GP surgery",
                    ["Never recap or bend needles", "Free sharps containers available from pharmacies"],
                    ["Never place loose in household waste or recycling", "Risk of needle-stick injury to waste workers"])),

            # ── T ──
            WasteItem("Tea Bags", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Compost or add to green waste bin (check for plastic mesh first)",
                    ["Plastic-free paper tea bags can go straight in compost", "Used tea is a mild fertiliser"],
                    ["Some brands contain polypropylene mesh – check before composting"])),
            WasteItem("Tin Foil Tray", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Rinse clean and recycle with metals",
                    ["Ball up with other foil pieces", "Clean trays are accepted in most metal recycling streams"],
                    ["Heavily soiled trays should go in general waste"])),
            WasteItem("Toothbrush (Plastic)", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Check for manufacturer mail-in recycling programme (e.g. TerraCycle)",
                    ["Switch to a bamboo toothbrush to reduce plastic waste", "Some councils collect them at civic amenity sites"],
                    ["Cannot go in kerbside recycling – too small and mixed materials"])),
            WasteItem("TV (Old)", WasteCategory.ELECTRONIC_WASTE,
                DisposalGuide(
                    "Take to a council recycling centre or arrange a large item collection",
                    ["Retailers must accept old TVs when delivering a new one under WEEE regulations", "Donate if still working"],
                    ["Never place in general household waste", "Contains hazardous materials including lead"])),

            # ── U ──
            WasteItem("Used Cooking Oil", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Collect in a sealed container and drop off at a local cooking oil recycling point or biodiesel facility",
                    ["Many council sites and some supermarkets have cooking oil collection points", "Can be used to make homemade soap"],
                    ["Never pour down the drain", "Do not mix with motor oil"])),

            # ── V ──
            WasteItem("Vegetable Peelings", WasteCategory.BIODEGRADABLE,
                DisposalGuide(
                    "Add to compost bin, food waste caddy, or green waste collection",
                    ["Mix with carbon-rich material like cardboard for balanced compost", "Can be buried directly in garden beds"],
                    [])),
            WasteItem("Vinyl Records (Damaged)", WasteCategory.NON_BIODEGRADABLE,
                DisposalGuide(
                    "Check specialist vinyl recycling programmes or creative reuse before landfill",
                    ["Undamaged records can be donated or sold", "Vinyl is PVC – not accepted in standard plastic recycling"],
                    ["Check local council for specific guidance"])),

            # ── W ──
            WasteItem("Window Glass (Broken)", WasteCategory.CONSTRUCTION,
                DisposalGuide(
                    "Wrap securely and take to a council recycling centre construction waste skip",
                    ["Label package 'sharp glass' clearly", "Separate from bottle/container glass – different composition"],
                    ["Never place in household glass recycling or wheelie bin", "Risk of injury to waste collectors"])),
            WasteItem("Wood Scraps", WasteCategory.CONSTRUCTION,
                DisposalGuide(
                    "Take to a council recycling centre or arrange a bulky waste collection",
                    ["Untreated wood can be composted or chipped for garden use", "Small pieces can be used as kindling"],
                    ["Treated, painted, or varnished wood must go to a licensed waste facility"])),

            # ── X ──
            WasteItem("X-Ray Film (Old)", WasteCategory.MEDICAL,
                DisposalGuide(
                    "Return to the hospital that issued it or contact a specialist x-ray film recycler",
                    ["Some companies extract silver from old films as part of the recycling process", "Never just throw in general waste"],
                    ["Contains silver halide compounds – requires specialist handling"])),

            # ── Y ──
            WasteItem("Yoghurt Pot (Plastic)", WasteCategory.RECYCLABLE,
                DisposalGuide(
                    "Rinse and place in plastic recycling bin",
                    ["Remove foil lid and recycle separately with metal foil", "Check for recycling symbol – most pots are #5 PP"],
                    [])),

            # ── Z ──
            WasteItem("Zinc Oxide Batteries", WasteCategory.HAZARDOUS,
                DisposalGuide(
                    "Collect and drop off at a battery recycling point",
                    ["Common in hearing aids and button cells", "Many pharmacies and electronics stores have collection boxes"],
                    ["Do not dispose of in general household waste", "Contains zinc and manganese – toxic if landfilled"])),
        ]

        # Store sorted alphabetically by name for consistent ordering
        for item in sorted(items, key=lambda i: i.name.lower()):
            self._items[item.name.lower()] = item

    # ── Query methods ────────────────────────────────────────────────────────
    def get_item(self, name: str) -> WasteItem | None:
        return self._items.get(name.strip().lower())

    def get_all_items(self) -> list[WasteItem]:
        return list(self._items.values())

    def search_by_name(self, query: str) -> list[WasteItem]:
        """Return all items whose name contains the query string (case-insensitive)."""
        q = query.strip().lower()
        return [item for item in self._items.values() if q in item.name.lower()]

    def get_items_by_category(self, category: WasteCategory) -> list[WasteItem]:
        """Return all items belonging to the given category."""
        return [item for item in self._items.values() if item.category == category]
