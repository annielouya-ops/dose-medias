"""Lot du 23 novembre 2026 (forfait gratuit Metricool, 1 carrousel par jour ouvré à 18 h).
Usage : python3 lot_2026-11-23.py <dossier_de_travail> [ids...]
Novembre est plein (20/20). Ce lot couvre le trou du 2 au 8/12 (le 1er/12 est déjà programmé).
Rotation après 27/11 crème puis 1er/12 marine : pour garder 3 couleurs différentes sur 3 posts consécutifs,
la suite est sauge -> crème -> marine -> sauge -> crème.
 2/12 sauge d01 | 3/12 crème d02 (VOTE) | 4/12 marine d03 | 7/12 sauge d04 | 8/12 crème d05
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
MMA = "Baromètre Fondation MMA des Entrepreneurs du Futur / Bpifrance Le Lab, juin 2025 (1 515 dirigeants)"
FID = "Baromètre des TPE Ifop / Fiducial n°84, juillet 2026 (1 003 dirigeants)"
AG2R = "Baromètre AG2R La Mondiale / Ipsos bva, septembre 2026 (307 dirigeants)"
YD = "Yerkes &amp; Dodson, Journal of Comparative Neurology and Psychology, 1908"
CIR = "Francesco Cirillo, The Pomodoro Technique (méthode créée à la fin des années 1980)"

posts = []
P = lambda **k: posts.append(k)

# Mercredi 2/12 — sauge, Énergie du dirigeant, check-list
P(id="d01", slug="2026-12-02_decembre-sur-la-reserve", date="2026-12-02T18:00:00", theme="sauge", pilier="Énergie du dirigeant",
  title="Tu attaques décembre sur la réserve ?",
  text="66 % des dirigeants travaillent plus de 45 heures par semaine. Et décembre arrive avec ses bouclages. 4 signes que tu attaques le mois sur la réserve. Tu en coches au moins 1 ? Oui ou non ?\n\n#energie #findannee " + H,
  slides=[cover("Tu attaques décembre sur la réserve&nbsp;?", "4 signes à repérer avant le rush."),
   s(f"<div class='big'>66&nbsp;%</div><p>des dirigeants travaillent plus de 45 heures par semaine. Et décembre n'a pas encore commencé.</p><div class='src'>{MMA}</div>"),
   num(1, "Ta liste de «&nbsp;avant Noël&nbsp;» s'allonge chaque jour.", "Tout doit être bouclé, rien n'est prévu pour toi."),
   num(2, "Tu dis «&nbsp;je me reposerai en janvier&nbsp;».", "Janvier a, lui aussi, ses urgences."),
   num(3, "Tu as zappé ta dernière vraie pause.", "Celle où tu ne pensais pas à ta boîte."),
   num(4, "Les petites contrariétés te pèsent plus que d'habitude.", "Souvent, c'est ta batterie qui parle."),
   cta("Tu en coches au moins&nbsp;1&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Jeudi 3/12 — crème, Coulisses, VOTE avec conséquence (le sujet gagnant sort le jeudi 10/12)
P(id="d02", slug="2026-12-03_vote-sujet-de-decembre", date="2026-12-03T18:00:00", theme="creme", pilier="Coulisses",
  title="C'est encore toi qui choisis",
  text="Coulisses : le prochain sujet, c'est toi qui le choisis. 1 = ton téléphone le soir. 2 = préparer ta semaine en 15 minutes. Écris 1 ou 2 en commentaire : le gagnant sort jeudi prochain.\n\n#coulisses #vote " + H,
  slides=[cover("C'est encore toi qui choisis.", "Le prochain sujet se décide en commentaire.", "Coulisses"),
   s("<h2>Ici, on construit une méthode pour les dirigeants.</h2><p class='it'>Alors autant partir de ce qui te bloque, toi.</p>"),
   s("<div class='kicker'>Option 1</div><h2>Ton téléphone, le soir.</h2><p class='it'>Comment arrêter de «&nbsp;juste vérifier&nbsp;» tes messages à 22&nbsp;h.</p>"),
   s("<div class='kicker'>Option 2</div><h2>Ta semaine en 15 minutes.</h2><p class='it'>Le rituel du lundi pour savoir où tu vas avant d'ouvrir tes mails.</p>"),
   s("<h2>Le sujet qui a le plus de voix sort jeudi prochain, à 18&nbsp;h.</h2><p class='it'>L'autre attendra son tour.</p>"),
   cta("Tu votes 1 ou&nbsp;2&nbsp;?", "Écris ton chiffre en commentaire." + ABO)])

# Vendredi 4/12 — marine, Juste dose, méthode nommée
P(id="d03", slug="2026-12-04_methode-pomodoro", date="2026-12-04T18:00:00", theme="marine", pilier="Juste dose",
  title="La méthode Pomodoro en 4 étapes",
  text="25 minutes de concentration, 5 minutes de pause : la méthode Pomodoro a été inventée par un étudiant avec un minuteur de cuisine. 4 étapes pour l'appliquer à ta journée de dirigeant. Tu l'as déjà essayée ? Oui ou non ?\n\n#productivite #organisation " + H,
  slides=[cover("La méthode Pomodoro", "Un minuteur de cuisine contre les journées hachées."),
   s(f"<h2>Inventée par un étudiant avec un minuteur en forme de tomate.</h2><p class='it'>«&nbsp;Pomodoro&nbsp;», c'est «&nbsp;tomate&nbsp;» en italien.</p><div class='src'>{CIR}</div>"),
   num(1, "Choisis une seule tâche.", "Le devis, le bilan, l'appel difficile. Pas trois à la fois."),
   num(2, "25 minutes, sans interruption.", "Téléphone retourné, mails fermés. Ce qui arrive est noté pour plus tard."),
   num(3, "5 minutes de vraie pause.", "Tu te lèves, tu respires. Pas d'écran."),
   num(4, "Après 4 tours, une pause plus longue.", "15 à 30 minutes. Tu l'as méritée."),
   cta("Tu l'as déjà essayée&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Lundi 7/12 — sauge, Juste dose, auto-évaluation de fin d'année
P(id="d04", slug="2026-12-07_bilan-2026-en-4-questions", date="2026-12-07T18:00:00", theme="sauge", pilier="Juste dose",
  title="Ton bilan 2026 en 4 questions",
  text="Avant de fixer tes objectifs 2027, fais le bilan de ton année de dirigeant. 4 questions simples, 15 minutes, un carnet. Tu fais ton bilan avant le 31 ? Oui ou non ?\n\n#bilan #findannee " + H,
  slides=[cover("Ton bilan 2026 en 4 questions", "Avant de penser 2027."),
   s(f"<div class='big'>13&nbsp;%</div><p>des dirigeants de TPE ne prennent aucun jour de congé dans l'année.</p><div class='src'>{FID}</div>"),
   num(1, "Qu'est-ce qui m'a donné le plus d'énergie&nbsp;?", "Un client, un projet, une décision. À garder en 2027."),
   num(2, "Qu'est-ce que je ne referais pas&nbsp;?", "Pas pour culpabiliser. Pour ne pas le répéter."),
   num(3, "Quelle tâche je ne veux plus faire moi-même&nbsp;?", "C'est ta première délégation de 2027."),
   num(4, "Combien de vrais jours off j'ai pris&nbsp;?", "Des jours sans mails. Le chiffre parle de lui-même."),
   cta("Tu fais ton bilan avant le&nbsp;31&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Mardi 8/12 — crème, Dose de réalité, idée reçue sourcée
P(id="d05", slug="2026-12-08_stress-ca-motive", date="2026-12-08T18:00:00", theme="creme", pilier="Dose de réalité",
  title="Le stress, ça motive ?",
  text="« Moi, je bosse mieux sous pression. » Vrai… jusqu'à un certain point. Depuis 1908, on sait qu'un peu de pression aide et que trop finit par freiner. Toi, la pression : A (elle te booste) ou B (elle te bloque) ?\n\n#stress #equilibre " + H,
  slides=[cover("Le stress, ça motive&nbsp;?", "«&nbsp;Moi, je bosse mieux sous pression.&nbsp;»", "Dose de réalité"),
   s(f"<h2>Vrai… jusqu'à un certain point.</h2><p>Dès 1908, des chercheurs observent qu'un peu de pression améliore la performance. Trop la fait chuter.</p><div class='src'>{YD}</div>"),
   s("<h2>C'est une courbe en cloche.</h2><p class='it'>Pas assez&nbsp;: tu t'ennuies. Juste ce qu'il faut&nbsp;: tu avances. Trop&nbsp;: tu bloques.</p>"),
   s(f"<div class='big'>17&nbsp;%</div><p>des dirigeants de TPE-PME vivent des périodes de stress intense au quotidien.</p><div class='src'>{AG2R}</div>"),
   s("<h2>Le stress n'est ni bon ni mauvais.</h2><p>C'est une question de dose. Et la tienne n'est pas celle du voisin.</p>"),
   cta("La pression&nbsp;: A ou&nbsp;B&nbsp;?", "A = elle te booste.<br>B = elle te bloque." + ABO)])

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
