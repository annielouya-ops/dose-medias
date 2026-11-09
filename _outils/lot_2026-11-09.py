"""Lot du 9 novembre 2026 (forfait gratuit Metricool, 1 carrousel par jour ouvré à 18 h).
Usage : python3 lot_2026-11-09.py <dossier_de_travail> [ids...]
Planning 16-27/11 (rotation après dormir-moins, marine, 13/11) :
 16 crème fermer-ta-journee (stock) | 17 sauge to-do-irrealiste (stock) | 18 marine GAGNANT DU VOTE (n01 ou n02)
 19 crème dose-en-3-mots (stock) | 20 sauge dire-non (stock) | 23 marine tout-est-important (stock)
 24 crème n03 | 25 sauge n04 | 26 marine dirigeant-gere-seul (stock) | 27 crème n05
Le sujet perdant du vote est gardé pour décembre (1er/12, marine).
"""
import json, subprocess, os, sys
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render.py")
W = sys.argv[1] if len(sys.argv) > 1 else "."
G = "<p class='src' style='font-size:30px;margin-top:40px'>Glisse &rarr;</p>"
def cover(h1, sub="", kicker=""):
    k = f"<div class='kicker'>{kicker}</div>" if kicker else ""
    s = f"<div class='rule'></div><p class='it'>{sub}</p>" if sub else ""
    return {"cls": "center", "nofoot": True, "html": "{DROP_L}" + k + f"<h1>{h1}</h1>" + s + G}
def cta(h2, p):
    return {"cls": "center", "nofoot": True, "html": "{DROP_L}" + f"<h2>{h2}</h2><div class='rule'></div><p>{p}</p>"}
def s(html): return {"html": html}
def num(i, a, b): return s(f"<div class='num'>0{i}</div><h2>{a}</h2><p class='it'>{b}</p>")
ABO = "<br>Et abonne-toi pour la suite."
H = "#entrepreneur #chefdentreprise #tpe #justedose"
GAL = "Gallup, étude sur 143 PDG du classement Inc. 500, 2015"
SCU = "Scullin et al., Journal of Experimental Psychology: General, 2018 (57 participants)"
MS = "Microsoft Work Trend Index, 2023 (31 000 personnes, 31 pays)"
BRA = "Bravata et al., Journal of General Internal Medicine, 2020 (synthèse de 62 études)"

posts = []
P = lambda **k: posts.append(k)

# Option 1 du vote (11/11) : prévue le mercredi 18/11 si elle gagne
P(id="n01", slug="2026-11-18_deleguer-sans-tout-perdre", date="2026-11-18T18:00:00", theme="marine", pilier="Juste dose",
  title="Déléguer sans tout perdre",
  text="Tu l'as choisi en commentaire : déléguer sans tout perdre. 4 étapes pour lâcher une tâche sans lâcher le contrôle de ta boîte. Tu délègues déjà une tâche par semaine ? Oui ou non ?\n\n#delegation #organisation " + H,
  slides=[cover("Déléguer sans tout perdre", "4 étapes pour lâcher une tâche, pas le contrôle."),
   s(f"<div class='big'>+33&nbsp;%</div><p>de chiffre d'affaires pour les dirigeants les plus doués pour déléguer, dans une étude sur des entreprises en forte croissance.</p><div class='src'>{GAL}</div>"),
   num(1, "Choisis la bonne tâche.", "Récurrente, bien connue, et qui n'est pas ta valeur ajoutée."),
   num(2, "Décris le résultat, pas la méthode.", "«&nbsp;Le devis part vendredi&nbsp;», pas «&nbsp;fais comme moi&nbsp;»."),
   num(3, "Fixe un point d'étape.", "Un rendez-vous court à mi-parcours. Pas une surveillance permanente."),
   num(4, "Accepte le «&nbsp;différent&nbsp;».", "Différent de toi ne veut pas dire moins bien."),
   cta("Tu délègues déjà une tâche par semaine&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Option 2 du vote : gardée pour le 1er/12 (ou avancée au 18/11 si elle gagne)
P(id="n02", slug="2026-12-01_tete-qui-tourne-le-soir", date="2026-12-01T18:00:00", theme="marine", pilier="Énergie du dirigeant",
  title="Ta tête tourne encore à minuit ?",
  text="Ta tête refait ta journée au moment de dormir ? Dans une étude, écrire sa to-do du lendemain pendant 5 minutes a aidé à s'endormir plus vite. Tu as un carnet près de ton lit ? Oui ou non ?\n\n#sommeil #energie " + H,
  slides=[cover("Ta tête tourne encore à minuit&nbsp;?", "Un test simple, mené en laboratoire."),
   s(f"<h2>5 minutes d'écriture avant de dormir.</h2><p class='it'>Un groupe note ce qu'il a fait dans la journée. L'autre, ce qu'il doit faire demain.</p><div class='src'>{SCU}</div>"),
   s(f"<div class='big'>9&nbsp;min</div><p>plus vite endormis, en moyenne, pour ceux qui avaient écrit leur to-do du lendemain.</p><div class='src'>{SCU}</div>"),
   s(f"<h2>Plus la liste était précise, plus ils s'endormaient vite.</h2><p class='it'>Vider ta tête sur le papier, c'est lui donner la permission de lâcher.</p><div class='src'>{SCU}</div>"),
   s("<div class='kicker'>Ce soir, essaie</div><ul><li>Un carnet près du lit, pas ton téléphone.</li><li>5 minutes&nbsp;: tout ce qui reste à faire demain.</li><li>Une ligne par tâche, la plus précise possible.</li></ul>"),
   s("<h2>Une petite étude, pas une baguette magique.</h2><p class='it'>Si tes nuits restent difficiles, parles-en à ton médecin.</p>"),
   cta("Tu as un carnet près de ton lit&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Mardi 24/11
P(id="n03", slug="2026-11-24_dose-fait-le-poison", date="2026-11-24T18:00:00", theme="creme", pilier="Juste dose",
  title="C'est la dose qui fait le poison",
  text="« C'est la dose qui fait le poison. » Paracelse l'écrivait en 1538, et ça vaut pour ta semaine de dirigeant. Ta dose de travail cette semaine : A (juste dose) ou B (overdose) ?\n\n#equilibre #energie " + H,
  slides=[cover("C'est la dose qui fait le poison.", "Une phrase de 1538 qui parle de ta semaine."),
   s("<h2>«&nbsp;Tout est poison, rien n'est sans poison&nbsp;; seule la dose fait qu'une chose n'est pas un poison.&nbsp;»</h2><div class='src'>Paracelse, Septem Defensiones, 1538</div>"),
   s("<h2>Le travail n'est pas le problème.</h2><p class='it'>C'est la dose. Un rush de temps en temps, ça passe. Toute l'année, ça use.</p>"),
   s("<div class='kicker'>Même logique pour</div><ul><li>Les réunions.</li><li>Les écrans le soir.</li><li>Les «&nbsp;oui&nbsp;» donnés trop vite.</li><li>Le téléphone en vacances.</li></ul>"),
   s("<h2>La bonne question n'est pas «&nbsp;bon ou mauvais&nbsp;?&nbsp;»</h2><p>C'est&nbsp;: quelle est <b>ta</b> juste dose&nbsp;?</p>"),
   cta("Ta semaine&nbsp;: A ou&nbsp;B&nbsp;?", "A = juste dose.<br>B = overdose." + ABO)])

# Mercredi 25/11
P(id="n04", slug="2026-11-25_avant-une-reunion", date="2026-11-25T18:00:00", theme="sauge", pilier="Juste dose",
  title="4 questions avant d'accepter une réunion",
  text="Les réunions inefficaces arrivent en tête des freins à la productivité dans l'enquête Microsoft 2023. 4 questions à te poser avant d'en accepter une. Tu as une réunion de trop cette semaine ? Oui ou non ?\n\n#reunion #organisation " + H,
  slides=[cover("4 questions avant d'accepter une réunion", "Ton agenda te dira merci."),
   s(f"<div class='big'>N°1</div><p>Les réunions inefficaces arrivent en tête des freins à la productivité cités par les salariés.</p><div class='src'>{MS}</div>"),
   num(1, "Quel est l'objectif, en une phrase&nbsp;?", "Pas d'objectif clair, pas de réunion."),
   num(2, "Est-ce que j'y suis indispensable&nbsp;?", "Un compte rendu suffit parfois."),
   num(3, "Un message suffirait-il&nbsp;?", "Beaucoup de réunions sont des mails qui ont pris rendez-vous."),
   num(4, "Peut-elle durer moitié moins&nbsp;?", "30 minutes au lieu d'une heure. Souvent, personne ne le remarque."),
   cta("Tu as une réunion de trop cette semaine&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Vendredi 27/11
P(id="n05", slug="2026-11-27_syndrome-imposteur", date="2026-11-27T18:00:00", theme="creme", pilier="Dose de réalité",
  title="Imposteur dans ta propre boîte ?",
  text="Réussir et avoir l'impression de ne pas le mériter : le phénomène de l'imposteur a un nom depuis 1978, et tu es loin d'être seul. Tu l'as déjà ressenti ? Oui ou non ?\n\n#syndromedelimposteur #confiance " + H,
  slides=[cover("Imposteur dans ta propre boîte&nbsp;?", "", "Dose de réalité"),
   s("<h2>Le phénomène a un nom depuis 1978.</h2><p>Réussir, et avoir l'impression de ne pas le mériter.</p><div class='src'>Clance &amp; Imes, Psychotherapy: Theory, Research &amp; Practice, 1978</div>"),
   s(f"<div class='big' style='font-size:190px;white-space:nowrap'>9 à 82&nbsp;%</div><p>C'est la part de personnes concernées selon les études. L'écart est énorme, mais tu es loin d'être un cas isolé.</p><div class='src'>{BRA}</div>"),
   s("<div class='kicker'>Signes fréquents</div><ul><li>Tu mets tes réussites sur le compte de la chance.</li><li>Tu as peur d'être «&nbsp;démasqué&nbsp;».</li><li>Tu prépares tout deux fois plus que nécessaire.</li></ul>"),
   s("<h2>Douter ne veut pas dire être illégitime.</h2><p class='it'>Ça veut souvent dire que tu prends ton rôle au sérieux.</p>"),
   cta("Tu l'as déjà ressenti&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

os.makedirs(f"{W}/specs", exist_ok=True)
only = set(sys.argv[2:])
for p in posts:
    if only and p["id"] not in only: continue
    f = f"{W}/specs/{p['id']}.json"
    json.dump({"theme": p["theme"], "slides": p["slides"]}, open(f, "w"), ensure_ascii=False)
    subprocess.run(["python3", "-I", R, f, f"{W}/out/{p['id']}"], check=True)
json.dump([{k: p[k] for k in ("id", "slug", "date", "theme", "pilier", "title", "text")} | {"n": len(p["slides"])} for p in posts],
          open(f"{W}/posts.json", "w"), ensure_ascii=False, indent=1)
print("done")
