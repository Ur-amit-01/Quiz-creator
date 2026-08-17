"""
Question bank: NEET (UG)-2024 (Code T3) - Biology (Solved Answers).

63 questions parsed from NEET (UG)-2024 (Code T3)'s solved-answers compilation.
Match-the-following and diagram-based questions were excluded at the
source (per the original compilation), since they require an image.

Each entry:
    question           -> str, <= 300 chars (Telegram poll limit)
    options             -> list[str], 2-10 items, each <= 100 chars
    correct_option_id   -> int, 0-indexed position in `options`
    explanation         -> str, <= 200 chars, shown after answering (optional)
"""

QUESTIONS = [
    {
        "question": "Identify the set of correct statements about pollination in hydrophytes: A. The flowers of Vallisneria are colourful and produce nectar. B. The flowers of waterlily are not pollinated by water. C. In most of water-pollinated species, the pollen grains are protected from wetting. D. Pollen grains of some hydrophytes are long and ribbon like. E. In some hydrophytes, the pollen grains are carried passively inside water.",
        "options": ["A, C, D and E only", "B, C, D and E only", "C, D and E only", "A, B, C and D only"],
        "correct_option_id": 1,
        "explanation": "Water-pollinated flowers (e.g., Vallisneria, Hydrilla) are inconspicuous, colourless and nectarless (so A is false); waterlily is insect-pollinated (B true); pollen is mucilage-protected from wetting (C true); marine forms like Zostera have ribbon-like pollen (D true); and pollen of species like Vallisneria is carried passively underwater (E true).",
    },
    {
        "question": "The type of conservation in which the threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called;",
        "options": ["Semi-conservative method", "Sustainable development", "in-situ conservation", "Biodiversity conservation"],
        "correct_option_id": 3,
        "explanation": "This describes ex-situ conservation (protection outside the natural habitat, e.g., zoos, botanical gardens, gene banks) — a key strategy under overall biodiversity conservation, unlike in-situ conservation which protects species within their natural habitat.",
    },
    {
        "question": "Inhibition of Succinic dehydrogenase enzyme by malonate is a classical example of:",
        "options": ["Competitive inhibition", "Enzyme activation", "Cofactor inhibition", "Feedback inhibition"],
        "correct_option_id": 0,
        "explanation": "Malonate closely resembles the substrate succinate in structure and competes with it for the active site of succinate dehydrogenase, making this a textbook example of competitive inhibition.",
    },
    {
        "question": "Bulliform cells are responsible for",
        "options": ["Increased photosynthesis in monocots.", "Providing large spaces for storage of sugars.", "Inward curling of leaves in monocots.", "Protecting the plant from salt stress."],
        "correct_option_id": 2,
        "explanation": "Large, thin-walled bulliform cells on the upper epidermis of grass leaves lose turgidity under water stress, causing the leaf to curl inward and minimise water loss.",
    },
    {
        "question": "Which of the following are required for the dark reaction of photosynthesis? A. Light B. Chlorophyll C. CO2 D. ATP E. NADPH",
        "options": ["C, D and E only", "D and E only", "A, B and C only", "B, C and D only"],
        "correct_option_id": 0,
        "explanation": "The dark (light-independent) reactions of the Calvin cycle need CO2 as the substrate and the ATP and NADPH generated during the light reaction; light and chlorophyll are not directly required in this phase.",
    },
    {
        "question": "Formation of interfascicular cambium from fully developed parenchyma cells is an example for",
        "options": ["Dedifferentiation", "Maturation", "Differentiation", "Redifferentiation"],
        "correct_option_id": 0,
        "explanation": "Living, fully differentiated parenchyma cells regaining the capacity to divide (forming cambium) is a classic example of dedifferentiation.",
    },
    {
        "question": "Hind II always cuts DNA molecules at a particular point called recognition sequence and it consists of:",
        "options": ["4 bp", "10 bp", "8 bp", "6 bp"],
        "correct_option_id": 3,
        "explanation": "HindII recognises the palindromic hexanucleotide sequence GTY^RAC, i.e., a 6 base pair recognition site.",
    },
    {
        "question": "Tropical regions show greatest level of species richness because A. Tropical latitudes have remained relatively undisturbed for millions of years, hence more time was available for species diversification. B. Tropical environments are more seasonal. C. More solar energy is available in tropics. D. Constant environments promote niche specialization. E. Tropical environments are constant and predictable.",
        "options": ["A, B and E only", "A, B and D only", "A, C, D and E only", "A and B only"],
        "correct_option_id": 2,
        "explanation": "Tropics have had long, undisturbed evolutionary time (A), receive more solar energy supporting higher productivity (C), and their relatively constant, predictable climate (E) promotes niche specialisation (D), together explaining higher species richness; tropics are less (not more) seasonal, so B is false.",
    },
    {
        "question": "Which one of the following is not a criterion for classification of fungi?",
        "options": ["Mode of spore formation", "Fruiting body", "Morphology of mycelium", "Mode of nutrition"],
        "correct_option_id": 3,
        "explanation": "Fungi are classified into classes mainly based on the nature/morphology of the mycelium, mode of spore formation, and fruiting bodies; mode of nutrition is not used as the classificatory criterion.",
    },
    {
        "question": "How many molecules of ATP and NADPH are required for every molecule of CO2 fixed in the Calvin cycle?",
        "options": ["3 molecules of ATP and 3 molecules of NADPH", "3 molecules of ATP and 2 molecules of NADPH", "2 molecules of ATP and 3 molecules of NADPH", "2 molecules of ATP and 2 molecules of NADPH"],
        "correct_option_id": 1,
        "explanation": "For every CO2 fixed in the Calvin cycle, 3 ATP and 2 NADPH are consumed.",
    },
    {
        "question": "These are regarded as major causes of biodiversity loss: A. Over exploitation B. Co-extinction C. Mutation D. Habitat loss and fragmentation E. Migration",
        "options": ["A, B and E only", "A, B and D only", "A, C and D only", "A, B, C and D only"],
        "correct_option_id": 1,
        "explanation": "The well-recognised major causes of biodiversity loss include habitat loss and fragmentation, over-exploitation, and co-extinction (along with alien species invasion, not listed here); mutation and migration are not counted among these major causes.",
    },
    {
        "question": "The capacity to generate a whole plant from any cell of the plant is called:",
        "options": ["Differentiation", "Somatic hybridization", "Totipotency", "Micropropagation"],
        "correct_option_id": 2,
        "explanation": "Totipotency is the inherent capacity of any living plant cell to regenerate into a complete organism under suitable conditions.",
    },
    {
        "question": "The equation of Verhulst-Pearl logistic growth is dN/dt = rN[(K-N)/K]. From this equation, K indicates:",
        "options": ["Carrying capacity", "Population density", "Intrinsic rate of natural increase", "Biotic potential"],
        "correct_option_id": 0,
        "explanation": "In the logistic growth equation, K represents the carrying capacity — the maximum population size that a given environment can sustain.",
    },
    {
        "question": "Spindle fibers attach to kinetochores of chromosomes during",
        "options": ["Anaphase", "Telophase", "Prophase", "Metaphase"],
        "correct_option_id": 3,
        "explanation": "At metaphase, spindle fibres from opposite poles attach to the kinetochores of chromosomes, aligning them at the equatorial plate.",
    },
    {
        "question": "In a plant, black seed color (BB/Bb) is dominant over white seed color (bb). In order to find out the genotype of the black seed plant, with which of the following genotype will you cross it?",
        "options": ["Bb", "BB/Bb", "BB", "bb"],
        "correct_option_id": 3,
        "explanation": "Crossing the black-seeded plant with the homozygous recessive (bb) plant is a test cross — the ratio of black:white offspring reveals whether the black parent is homozygous (BB, all black progeny) or heterozygous (Bb, 1:1 black:white progeny).",
    },
    {
        "question": "A pink flowered Snapdragon plant was crossed with a red flowered Snapdragon plant. What type of phenotype/s is/are expected in the progeny?",
        "options": ["Only pink flowered plants", "Red, Pink as well as white flowered plants", "Only red flowered plants", "Red flowered as well as pink flowered plants"],
        "correct_option_id": 3,
        "explanation": "Snapdragon flower colour shows incomplete dominance (RR = red, Rr = pink, rr = white). Crossing pink (Rr) x red (RR) gives 1/2 RR (red) : 1/2 Rr (pink) — red and pink flowers only, no white.",
    },
    {
        "question": "Lecithin, a small molecular weight organic compound found in living tissues, is an example of:",
        "options": ["Glycerides", "Carbohydrates", "Amino acids", "Phospholipids"],
        "correct_option_id": 3,
        "explanation": "Lecithin (phosphatidylcholine) is a phospholipid, a key component of cell membranes.",
    },
    {
        "question": "Which of the following is an example of actinomorphic flower?",
        "options": ["Pisum", "Sesbania", "Datura", "Cassia"],
        "correct_option_id": 2,
        "explanation": "Datura has a radially symmetrical (actinomorphic) flower, unlike Pisum, Sesbania and Cassia, which are zygomorphic (bilaterally symmetrical).",
    },
    {
        "question": "A transcription unit in DNA is defined primarily by the three regions in DNA and these are with respect to upstream and down stream end;",
        "options": ["Inducer, Repressor, Structural gene", "Promotor, Structural gene, Terminator", "Repressor, Operator gene, Structural gene", "Structural gene, Transposons, Operator gene"],
        "correct_option_id": 1,
        "explanation": "A transcription unit consists of a promoter, the structural gene(s) to be transcribed, and a terminator marking the end of transcription.",
    },
    {
        "question": "What is the fate of piece of DNA carrying only gene of interest which is transferred into an alien organism? A. The piece of DNA would be able to multiply itself independently in the progeny cells of the organisms. B. It may get integrated into the genome of the recipient. C. It may multiply and be inherited along with the host DNA. D. The alien piece of DNA is not an integrated part of chromosome. E. It shows ability to replicate.",
        "options": ["B and C only", "A and E only", "A and B only", "D and E only"],
        "correct_option_id": 0,
        "explanation": "A DNA fragment carrying only the gene of interest (lacking its own origin of replication) cannot multiply independently; it must integrate into the recipient's genome, after which it multiplies and is inherited along with the host DNA.",
    },
    {
        "question": "Auxin is used by gardeners to prepare weed free lawns. But no damage is caused to grass as auxin;",
        "options": ["does not affect mature monocotyledonous plants.", "can help in cell division in grasses, to produce growth.", "promotes apical dominance.", "promotes abscission of mature leaves only."],
        "correct_option_id": 0,
        "explanation": "Synthetic auxins like 2,4-D selectively kill broad-leaved dicot weeds but do not affect mature monocot plants such as grasses, allowing weed-free lawns without harming the grass.",
    },
    {
        "question": "The cofactor of the enzyme carboxypeptidase is:",
        "options": ["Flavin", "Haem", "Zinc", "Niacin"],
        "correct_option_id": 2,
        "explanation": "Carboxypeptidase is a zinc-dependent metalloenzyme; zinc acts as its cofactor.",
    },
    {
        "question": "The lactose present in the growth medium of bacteria is transported to the cell by the action of",
        "options": ["Permease", "Polymerase", "Beta-galactosidase", "Acetylase"],
        "correct_option_id": 0,
        "explanation": "In the lac operon system, permease facilitates the transport of lactose into the bacterial cell.",
    },
    {
        "question": "Which one of the following can be explained on the basis of Mendel's Law of Dominance? A. Out of one pair of factors one is dominant and the other is recessive. B. Alleles do not show any expression and both the characters appear as such in F2 generation. C. Factors occur in pair in normal diploid plants. D. The discrete unit controlling a particular character is called factor. E. The expression of only one of the parental characters is found in a monohybrid cross.",
        "options": ["B, C and D only", "A, B, C, D and E", "A, B and C only", "A, C, D and E only"],
        "correct_option_id": 3,
        "explanation": "The Law of Dominance covers the concepts of discrete factors (D) occurring in pairs (C), one being dominant over the other (A), resulting in expression of only the dominant parental character in a monohybrid cross (E). Statement B describes co-dominance, not the law of dominance, so it is excluded.",
    },
    {
        "question": "Given below are two statements: Statement I: Bt toxins are insect group specific and coded by a gene cry IAc. Statement II: Bt toxin exists as inactive protoxin in B. thuringienis. However, after ingestion by the insect the inactive protoxin gets converted into active form due to acidic pH of the insect gut.",
        "options": ["Statement I is true but Statement II is false.", "Statement I is false but Statement II is true.", "Both Statement I and Statement II are true.", "Both Statement I and Statement II are false."],
        "correct_option_id": 0,
        "explanation": "Bt toxins (e.g., cry genes like cryIAc) are indeed insect-group specific, so Statement I is true. However, the inactive protoxin is converted to its active, toxic form due to the alkaline (not acidic) pH of the insect gut, so Statement II is false.",
    },
    {
        "question": "Given below are two statements: Statement I: Parenchyma is living but collenchyma is dead tissue. Statement II: Gymnosperms lack xylem vessels but presence of xylem vessels is the characteristic of angiosperms.",
        "options": ["Statement I is true but Statement II is false.", "Statement I is false but Statement II is true.", "Both Statement I and Statement II are true.", "Both Statement I and Statement II are false"],
        "correct_option_id": 1,
        "explanation": "Collenchyma, like parenchyma, is a living simple tissue (not dead), so Statement I is false. Gymnosperms typically possess only tracheids (lacking vessels), while vessels are a characteristic feature of angiosperm xylem, so Statement II is true.",
    },
    {
        "question": "Given below are two Statements: Statement I: Chromosomes become gradually visible under light microscope during leptotene stage. Statement II: The beginning of diplotene stage is recognized by dissolution of synaptonemal complex.",
        "options": ["Statement I is true but Statement II is false.", "Statement I is false but Statement II is true.", "Both Statement I and Statement II are true.", "Both Statement I and Statement II are false"],
        "correct_option_id": 2,
        "explanation": "During leptotene, chromosomes gradually condense and become visible under the light microscope; the onset of diplotene is marked by dissolution of the synaptonemal complex, allowing recombined homologous chromosomes to begin separating. Both statements are correct.",
    },
    {
        "question": "List of endangered species was released by-:",
        "options": ["Foam", "IUCN", "GEAC", "WWF"],
        "correct_option_id": 1,
        "explanation": "The IUCN (International Union for Conservation of Nature) publishes the Red List/list of endangered species.",
    },
    {
        "question": "The DNA present in chloroplast is:",
        "options": ["Linear, single stranded", "Circular, single stranded", "Linear, double stranded", "Circular, double stranded"],
        "correct_option_id": 3,
        "explanation": "Like mitochondrial DNA, chloroplast DNA is circular and double stranded, resembling bacterial DNA — consistent with the endosymbiotic origin of these organelles.",
    },
    {
        "question": "Which of the following are fused in somatic hybridization involving two varieties of plants?",
        "options": ["Protoplsats", "Pollens", "Callus", "Somatic embryos"],
        "correct_option_id": 0,
        "explanation": "Somatic hybridisation involves fusing protoplasts (cells stripped of their walls) of two different varieties/species to produce a hybrid.",
    },
    {
        "question": "Spraying sugarcane crop with which of the following plant growth regulators, increases the length of stem, thus, increasing the yield?",
        "options": ["Cytokinin", "Abscisic acid", "Auxin", "Gibberellin"],
        "correct_option_id": 3,
        "explanation": "Gibberellins increase stem/internode elongation; spraying sugarcane with gibberellins increases stem length and, consequently, cane/sugar yield.",
    },
    {
        "question": "Given below are two statements: Statement I: In C3 Plants, some O2 binds RuBisCO, hence CO2 fixation is decreased. Statement II: In C4 plants, mesophyll cells show very little photorespiration while bundle sheath cells do not show photorespiration.",
        "options": ["Statement I is true but Statement II is false.", "Statement I is false but Statement II is true.", "Both Statement I and Statement II are true.", "Both Statement I and Statement II are false"],
        "correct_option_id": 0,
        "explanation": "RuBisCO's oxygenase activity in C3 plants allows O2 to compete with CO2, reducing net CO2 fixation (Statement I true). In C4 plants, RuBisCO (and hence photorespiration) is essentially absent in the O2-poor mesophyll cells, while the CO2-rich bundle sheath cells largely suppress (not completely show or eliminate as stated) photorespiration — the statement's description is reversed, making Statement II false.",
    },
    {
        "question": "Identify the step in tricarboxylic acid cycle, which does not involve oxidation of substrate.",
        "options": ["Succinyl-CoA → Succinic acid", "Isocitrate → α-ketoglutaric acid", "Malic acid → Oxaloacetic acid", "Succinic acid → Malic acid"],
        "correct_option_id": 0,
        "explanation": "The conversion of succinyl-CoA to succinic acid is a substrate-level phosphorylation step (generating GTP/ATP) and does not involve any redox/oxidation reaction, unlike the other listed steps which are all oxidative (each producing NADH or FADH2).",
    },
    {
        "question": "Which of the following statement is correct regarding the process of replication in E.coli?",
        "options": ["The DNA dependent DNA polymerase catalyses polymerization in 5'→3' as well as 3'→5' direction.", "The DNA dependent DNA polymerase catalyses polymerization in 5'→3' direction.", "The DNA dependent DNA polymerase catalyses polymerization in one direction, that is 3'→5'.", "The DNA dependent RNA polymerase catalyase polymerization in one direction, that is 5'→3'."],
        "correct_option_id": 1,
        "explanation": "DNA polymerase can add nucleotides only in the 5'→3' direction, reading the template strand 3'→5'.",
    },
    {
        "question": "In an ecosystem if the Net Primary Productivity (NPP) of first trophic level is: 100x (kcal m⁻²) yr⁻¹ what would be the GPP (Gross Primary Productivity) of the third trophic level of the same ecosystem?",
        "options": ["10x (kcal m⁻²) yr⁻¹", "(100x/3x) (kcal m⁻²) yr⁻¹", "(x/10) (kcal m⁻²) yr⁻¹", "x (kcal m⁻²) yr⁻¹"],
        "correct_option_id": 3,
        "explanation": "Applying the 10% law successively: energy reaching the second trophic level ≈ 10% of 100x = 10x; energy reaching (and hence gross productivity of) the third trophic level ≈ 10% of 10x = x (kcal m⁻²) yr⁻¹.",
    },
    {
        "question": "Read the following statements and choose the set of correct statements. In the members of Phaeophyceae. A. Asexual reproduction occurs usually by biflagellate zoospores. B. Sexual reproduction is by oogamous method only. C. Stored food is in the form of carbohydrates which is either mannitol or laminarin. D. The major pigments found are chlorophyll a, c and carotenoids and xanthophyll. E. Vegetative cells have a cellulosic wall, usually covered on the outside by gelatinous coating of algin.",
        "options": ["A, C, D and E only", "A, B, C and E only", "A, B, C and D only", "B, C, D and E only"],
        "correct_option_id": 0,
        "explanation": "Phaeophyceae members reproduce asexually via biflagellate zoospores (A) and sexually by isogamous, anisogamous, or oogamous methods (not oogamous only, so B is false); they store food as mannitol/laminarin (C), contain chlorophyll a, c, carotenoids and fucoxanthin (a xanthophyll) (D), and have a cellulosic cell wall coated externally with algin (E).",
    },
    {
        "question": "Given below are two statements: Statement I: The presence or absence of hymen is not a reliable indicator of virginity. Statement II: The hymen is torn during the first coitus only.",
        "options": ["Statement I is true but Statement II is false.", "Statement I is false but Statement II is true.", "Both Statement I and Statement II are true.", "Both Statement I and Statement II are false."],
        "correct_option_id": 0,
        "explanation": "The hymen's presence/absence is not a reliable virginity indicator (Statement I true), as it can also be ruptured due to non-sexual physical activities, and does not necessarily tear only during first coitus, making Statement II false.",
    },
    {
        "question": "In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on:",
        "options": ["8th and 9th segment", "11th segment", "5th segment", "10th segment"],
        "correct_option_id": 3,
        "explanation": "In cockroaches, a pair of anal cerci is present on the 10th (last) abdominal segment.",
    },
    {
        "question": "Which of the following is not a steroid hormone?",
        "options": ["Progesterone", "Glucagon", "Cortisol", "Testosterone"],
        "correct_option_id": 1,
        "explanation": "Progesterone, cortisol and testosterone are steroid hormones; glucagon is a peptide hormone secreted by pancreatic alpha cells.",
    },
    {
        "question": "Which one is the correct product of DNA dependent RNA polymerase to the given template? 3' TACATGGCAAATATCCATTCA 5'",
        "options": ["5' AUGUACCGUUUAUAGGGAAGU 3'", "5' ATGTACCGTTTATAGGTAAGT 3'", "5' AUGUACCGUUUAUAGGUAAGU 3'", "5' AUGUAAAGUUUAUAGGUAAGU 3'"],
        "correct_option_id": 2,
        "explanation": "Transcribing the template (3'→5': TACATGGCAAATATCCATTCA) into complementary, antiparallel RNA (5'→3', using U for A-pairing) gives 5' AUGUACCGUUUAUAGGUAAGU 3'.",
    },
    {
        "question": "Following are the stages of cell division: A. Gap 2 phase B. Cytokinesis C. Synthesis phase D. Karyokinesis E. Gap 1 phase",
        "options": ["B-D-E-A-C", "E-C-A-D-B", "C-E-D-A-B", "E-B-D-A-C"],
        "correct_option_id": 1,
        "explanation": "The correct order is: Gap 1 (E) → Synthesis (C) → Gap 2 (A) → Karyokinesis/nuclear division (D) → Cytokinesis (B).",
    },
    {
        "question": "Which of the following are Autoimmune disorders? A. Myasthenia gravis B. Rheumatoid arthritis C. Gout D. Muscular dystrophy E. Systemic Lupus Erythematosus (SLE)",
        "options": ["B, C & E only", "C, D & E only", "A, B & D only", "A, B & E only"],
        "correct_option_id": 3,
        "explanation": "Myasthenia gravis, rheumatoid arthritis and SLE are autoimmune disorders (body's immune system attacks its own tissues); gout is a metabolic disorder and muscular dystrophy is a genetic disorder, not autoimmune.",
    },
    {
        "question": "The flippers of the Penguins and Dolphins are the example of the",
        "options": ["Convergent evolution", "Divergent evolution", "Adaptive radiation", "Natural selection"],
        "correct_option_id": 0,
        "explanation": "Flippers of penguins (birds) and dolphins (mammals) are analogous structures that evolved independently to perform a similar function (swimming) — a classic case of convergent evolution.",
    },
    {
        "question": "Which one of the following factors will not affect the Hardy-Weinberg equilibrium?",
        "options": ["Gene migration", "Constant gene pool", "Genetic recombination", "Genetic drift"],
        "correct_option_id": 1,
        "explanation": "Hardy-Weinberg equilibrium is disturbed by gene migration, genetic drift, mutation, recombination, and natural selection; a constant, unchanging gene pool is precisely the condition that maintains equilibrium, not disturbs it.",
    },
    {
        "question": "Given below are some stages of human evolution. Arrange them in correct sequence. (Past to Recent) A. Homo habilis B. Homo sapiens C. Homo neanderthalensis D. Homo erectus",
        "options": ["C-B-D-A", "A-D-C-B", "D-A-C-B", "B-A-D-C"],
        "correct_option_id": 1,
        "explanation": "The evolutionary sequence from past to recent is: Homo habilis → Homo erectus → Homo neanderthalensis → Homo sapiens.",
    },
    {
        "question": "Following are the stages of pathway for conduction of an action potential through the heart: A. AV bundle B. Purkinje fibres C. AV node D. Bundle branches E. SA node",
        "options": ["B-D-E-C-A", "E-A-D-B-C", "E-C-A-D-B", "A-E-C-B-D"],
        "correct_option_id": 2,
        "explanation": "The cardiac conduction pathway is: SA node (E) → AV node (C) → AV bundle (A) → Bundle branches (D) → Purkinje fibres (B).",
    },
    {
        "question": "Which of the following factors are favourable for the formation of oxyhaemoglobin in alveoli?",
        "options": ["Low pCO2 and High H+ concentration", "Low pCO2 and High temperature", "High pO2 and High pCO2", "High pO2 and Lesser H+ concentration"],
        "correct_option_id": 3,
        "explanation": "High pO2 and low H+ concentration (along with low pCO2 and low temperature) favour the binding of O2 to haemoglobin, forming oxyhaemoglobin in the alveoli.",
    },
    {
        "question": "Given below are two statement: one is labelled as Assertion A and the other is labelled as Reason R: Assertion A: FSH acts upon ovarian follicles in female and Leydig cells in male. Reason R: Growing ovarian follicles secrete estrogen in female while interstitial cells secrete androgen in male human being.",
        "options": ["A is true but R is false", "A is false but R is true", "Both A and R are true and R is the correct explanation of A.", "Both A and R are true but R is NOT the correct explanation of A."],
        "correct_option_id": 1,
        "explanation": "FSH acts on ovarian follicles in females but on Sertoli cells (not Leydig cells) in males — Leydig/interstitial cells are stimulated by LH — so Assertion A is false. Reason R, describing hormone secretion by ovarian follicles (estrogen) and interstitial/Leydig cells (androgen), is correct.",
    },
    {
        "question": "Consider the following statements: A. Annelids are true coelomates B. Poriferans are pseudocoelomates C. Aschelminithes are acoelomates D. Platyhelminthes are pseudocoelomates",
        "options": ["C only", "D only", "B only", "A only"],
        "correct_option_id": 3,
        "explanation": "Annelids are true coelomates (correct, A). Poriferans are acoelomate (not pseudocoelomate, B false), Aschelminthes/roundworms are pseudocoelomate (not acoelomate, C false), and Platyhelminthes are acoelomate (not pseudocoelomate, D false).",
    },
    {
        "question": "Given below are two statements: Statements I: In the nephron the descending limb of loop of Henle is impermeable to water and permeable to electrolytes. Statement II: The proximal convoluted tubule is lined by simple columnar brush border epithelium and increases the surface area for reabsorption.",
        "options": ["Statement I is true but Statement II is false.", "Statement I is false but Statement II is true.", "Both Statement I and Statement II are true.", "Both Statement I and Statement II are false."],
        "correct_option_id": 1,
        "explanation": "The descending limb of the loop of Henle is actually permeable to water and relatively impermeable to electrolytes (the reverse of Statement I, making it false), while the PCT is indeed lined by simple cuboidal/columnar brush border epithelium that increases the surface area for reabsorption (Statement II true).",
    },
    {
        "question": "Which of the following is not a natural/traditional contraceptive method?",
        "options": ["Lactational amenorrhea", "Vaults", "Coitus interruptus", "Periodic abstinence"],
        "correct_option_id": 1,
        "explanation": "Lactational amenorrhea, coitus interruptus and periodic abstinence are natural/traditional methods; vaults (cervical caps/diaphragms) are barrier contraceptive devices, not natural methods.",
    },
    {
        "question": "Which of the following statements is incorrect?",
        "options": ["Bio-reactors are used to produce small scale bacterial cultures.", "Bio-reactors have an agitator system, an oxygen delivery system and foam control system.", "A bio-reactor provides optimal growth conditions for achieving the desired product.", "Most commonly used bio-reactors are of stirring type."],
        "correct_option_id": 0,
        "explanation": "Bioreactors are used for large-scale production of the desired product from biological reactions, not small-scale cultures; the other statements correctly describe bioreactor features.",
    },
    {
        "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R: Assertion A: Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby. Reason R: Colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.",
        "options": ["A is correct but R is not correct.", "A is not correct but R is correct.", "Both A and R are correct and R is the correct explanation of A.", "Both A and R are correct but R is NOT the correct explanation of A."],
        "correct_option_id": 2,
        "explanation": "Breast-feeding, especially with early colostrum rich in antibodies, is recommended for a healthy baby, and the antibody content of colostrum is precisely the reason it builds the newborn's immune resistance.",
    },
    {
        "question": "The \"Ti plasmid\" of Agrobacterium tumefaciens stands for",
        "options": ["Tumor inducing plasmid", "Temperature independent plasmid", "Tumour inhibiting plasmid", "Tumor independent plasmid"],
        "correct_option_id": 0,
        "explanation": "\"Ti\" stands for Tumor-inducing plasmid, which is disarmed and used as a vector in plant genetic engineering.",
    },
    {
        "question": "Which of the following is not a component of Fallopian tube?",
        "options": ["Infundibulum", "Ampulla", "Uterine fundus", "Isthmus"],
        "correct_option_id": 2,
        "explanation": "The Fallopian tube comprises the infundibulum, ampulla and isthmus; the uterine fundus is a part of the uterus, not the Fallopian tube.",
    },
    {
        "question": "The following are the statements about non-chordates: A. Pharynx is perforated by gill slits. B. Notochord is absent. C. Central nervous system is dorsal. D. Heart is dorsal if present. E. Post anal tail is absent.",
        "options": ["B, D and E only", "B, C and D only", "A and C only", "A, B and D only"],
        "correct_option_id": 0,
        "explanation": "Non-chordates lack a notochord (B) and a post-anal tail (E), and their heart (when present) is dorsally located (D); pharyngeal gill slits (A) and a dorsal nerve cord (C) are chordate features, not non-chordate ones.",
    },
    {
        "question": "Given below are two statements: Statement I: The cerebral hemispheres are connected by nerve tract known as corpus callosum. Statement II: The brain stem consists of the medulla oblongata, pons and cerebrum.",
        "options": ["Statement I is correct but statement II is incorrect.", "Statement I is incorrect but statement II is correct.", "Both statement I and Statement II are correct.", "Both statement I and Statement II are incorrect."],
        "correct_option_id": 0,
        "explanation": "The two cerebral hemispheres are indeed connected by the corpus callosum (Statement I true). The brain stem consists of the midbrain, pons and medulla oblongata — not the cerebrum — making Statement II false.",
    },
    {
        "question": "Given below are two statements: Statement I: Bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced. Statement II: Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes.",
        "options": ["Statement I is correct but statement II is incorrect.", "Statement I is incorrect but statement II is correct.", "Both statement I and Statement II are correct.", "Both statement I and Statement II are incorrect."],
        "correct_option_id": 0,
        "explanation": "Bone marrow is indeed the primary lymphoid organ producing all blood cells including lymphocytes (Statement I true). However, T-lymphocytes mature specifically in the thymus, while bone marrow is where B-lymphocytes mature — so it is not accurate that both organs mature T-lymphocytes, making Statement II false.",
    },
    {
        "question": "Choose the correct statement given below regarding juxta medullary nephron.",
        "options": ["Loop of Henle of juxtamedullary nephron runs deep into medulla.", "Juxtamedullary nephrons outnumber the cortical nephtons.", "Juxtamedullary nephrons are located in the columns of Bertini.", "Renal corpuscle of juxtamedullary nephron lies in the outer portion of he renal medulla."],
        "correct_option_id": 0,
        "explanation": "Juxtamedullary nephrons have long loops of Henle that extend deep into the medulla; they are far fewer in number than cortical nephrons, and their renal corpuscles lie in the cortex, close to the medulla.",
    },
    {
        "question": "As per ABO blood grouping system, the blood group of fathers is B+, mother is A+ and child is O+. Their respective genotype can be A. I^B i / I^A i / ii B. I^B I^B / I^A I^A / ii C. I^A I^B / i I^A / I^B i D. I^A i / I^B i / I^A i E. i I^B / i I^A / I^A I^B",
        "options": ["C & B only", "D & E only", "A only", "B only"],
        "correct_option_id": 2,
        "explanation": "Since the child is blood group O (genotype ii), each parent must carry the recessive i allele. So the father (group B) must be I^B i and the mother (group A) must be I^A i, giving the child ii — this matches combination A only.",
    },
    {
        "question": "Given below are two statements: Statement I: Gause's competitive exclusive principle states that two closely related species competing for different resources cannot exist indefinitely. Statement II: According to Gause's principle, during competition, the inferior will be eliminated. This may be true if resources are limiting.",
        "options": ["Statement I is true but Statement II is false.", "Statement I is false but statement II is true.", "Both statement I and Statement II are true.", "Both statement I and Statement II are false."],
        "correct_option_id": 1,
        "explanation": "Gause's competitive exclusion principle actually applies to species competing for the SAME (limiting) resources, not different resources, making Statement I false; Statement II correctly describes the outcome of such competition — the competitively inferior species being eliminated when resources are limiting.",
    },
    {
        "question": "Regarding catalytic cycle of an enzyme action, select the correct sequential steps: A. Substrate enzyme complex formation. B. Free enzyme ready to bind with another substrate. C. Release of products. D. Chemical bonds of the substrate broken. E. Substrate binding to active site.",
        "options": ["B, A, C, D, E", "E, D, C, B, A", "E, A, D, C, B", "A, E, B, D, C"],
        "correct_option_id": 2,
        "explanation": "The catalytic cycle proceeds as: substrate binds to the active site (E) → substrate-enzyme complex forms (A) → chemical bonds of the substrate are broken (D) → products are released (C) → the free enzyme is ready to bind another substrate molecule (B).",
    },
    {
        "question": "Given below are two statements: Statement I: Mitochondria and chloroplasts are both double membrane bound organelles. Statement II: Inner membrane of mitochondria is relatively less permeable, as compared to chloroplast.",
        "options": ["Statement I is correct but statement II is incorrect.", "Statement I is incorrect but statement II is correct.", "Both statement I and Statement II are correct.", "Both statement I and Statement II are incorrect."],
        "correct_option_id": 2,
        "explanation": "Both mitochondria and chloroplasts are double membrane-bound organelles (Statement I true), and the inner mitochondrial membrane is relatively less permeable (highly selective, forming cristae) compared to the more permeable inner membrane of the chloroplast (Statement II true).",
    },
]
