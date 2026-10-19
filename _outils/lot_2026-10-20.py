"""Lot semaine 2 : carrousels du mardi 20 au lundi 26 octobre 2026.
Usage : python3 lot_2026-10-20.py <dossier_de_travail>
Rotation : dernier post coloré = marine (lundi 19, 18 h) -> on repart sur crème.
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
AG2R = "Baromètre AG2R La Mondiale / Ipsos bva, septembre 2026"
MARK = "Gloria Mark, université de Californie à Irvine, 2008"

posts = []
P = lambda **k: posts.append(k)

P(id="c01", slug="2026-10-20_dose-pour-toi-si", date="2026-10-20T10:00:00", theme="creme", pilier="Coulisses",
  title="DOSE, c'est pour toi si…",
  text="DOSE, c'est pour toi si tu as créé ta boîte pour être libre… et que ton agenda décide de tout à ta place. Tu te reconnais ? Écris 1 si oui, 2 si pas encore.\n\n#coulisses #lancement " + H,
  slides=[cover("DOSE, c'est pour toi si…", "Le lancement approche. Voici à qui on s'adresse.", "Coulisses"),
   num(1, "Tu as créé ta boîte pour être libre.", "Et ton agenda décide de tout à ta place."),
   num(2, "Tu dis «&nbsp;ça va&nbsp;» par réflexe.", "Même les semaines où ça ne va pas vraiment."),
   num(3, "Tu sais que tu devrais déléguer.", "Mais tu n'as jamais le temps d'expliquer."),
   num(4, "Tu veux durer, pas juste tenir.", "Ton entreprise a besoin de toi dans 10 ans aussi."),
   cta("Tu te reconnais&nbsp;?", "Écris 1 si oui, 2 si pas encore.<br>Et abonne-toi pour suivre le lancement.")])

P(id="c02", slug="2026-10-20_sprinteur-ou-marathonien", date="2026-10-20T18:00:00", theme="sauge", pilier="Énergie du dirigeant",
  title="Sprinteur ou marathonien ?",
  text="Tu fonces par à-coups ou tu avances à rythme régulier ? Aucun profil n'est parfait, mais l'un des deux use plus vite. Tu es plutôt A ou B ?\n\n#energie #organisation " + H,
  slides=[cover("Sprinteur ou marathonien&nbsp;?", "Ton rythme de travail en dit long."),
   s("<div class='kicker'>Profil A · Sprinteur</div><h2>Tu fonces par à-coups.</h2><ul><li>Des journées à 100&nbsp;%, puis le trou.</li><li>Tu boucles tout à la dernière minute.</li><li>Tu récupères quand tu n'as plus le choix.</li></ul>"),
   s("<div class='kicker'>Profil B · Marathonien</div><h2>Tu avances à rythme régulier.</h2><ul><li>Des journées pleines, jamais à vide.</li><li>Tu prévois de la marge.</li><li>Tu poses tes pauses avant d'en avoir besoin.</li></ul>"),
   s("<h2>Aucun profil n'est parfait.</h2><p class='it'>Le sprint use si tu n'en sors jamais. La régularité s'endort si rien ne la bouscule.</p>"),
   s("<div class='kicker'>La juste dose</div><h2>Des sprints choisis, sur une base régulière.</h2><p>Pas l'inverse.</p>"),
   cta("Tu es plutôt A ou&nbsp;B&nbsp;?", "Écris A ou B en commentaire." + ABO)])

P(id="c03", slug="2026-10-21_multitache", date="2026-10-21T10:00:00", theme="marine", pilier="Dose de réalité",
  title="Le multitâche te fait gagner du temps ?",
  text="Faire tout en même temps te fait gagner du temps ? Les chiffres disent l'inverse. Tu tiens 45 minutes sans interruption ? Oui ou non ?\n\n#productivite #concentration " + H,
  slides=[cover("Tout faire en même temps te fait gagner du temps&nbsp;?", "", "Dose de réalité"),
   s(f"<div class='big'>23&nbsp;min</div><p>C'est le temps moyen pour revenir à une tâche après une interruption.</p><div class='src'>{MARK}</div>"),
   s(f"<div class='big'>3&nbsp;min</div><p>Les salariés observés changeaient d'activité toutes les 3 minutes environ. Et la moitié du temps, de leur propre initiative.</p><div class='src'>{MARK}</div>"),
   s("<div class='big'>47&nbsp;s</div><p>C'est la durée moyenne d'attention sur un écran avant de passer à autre chose.</p><div class='src'>Gloria Mark, «&nbsp;Attention Span&nbsp;», 2023</div>"),
   s("<h2>Ton cerveau ne fait pas deux choses à la fois.</h2><p class='it'>Il saute de l'une à l'autre. Et chaque saut coûte.</p>"),
   s("<div class='kicker'>À tester cette semaine</div><h2>Une tâche. Un onglet. 45 minutes.</h2><p>Téléphone dans une autre pièce.</p>"),
   cta("Tu tiens 45 minutes sans interruption&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c04", slug="2026-10-21_idees-en-marchant", date="2026-10-21T18:00:00", theme="creme", pilier="Énergie du dirigeant",
  title="Tes meilleures idées arrivent en marchant",
  text="Tes meilleures idées n'arrivent pas à ton bureau. Marcher augmente en moyenne de 60 % la production d'idées (Stanford, 2014). Tu réfléchis mieux assis ou en marchant ? A ou B ?\n\n#energie #creativite " + H,
  slides=[cover("Tes meilleures idées n'arrivent pas à ton bureau.", "Et la science est plutôt d'accord."),
   s("<div class='big'>+60&nbsp;%</div><p>d'idées créatives, en moyenne, en marchant plutôt qu'assis.</p><div class='src'>Oppezzo &amp; Schwartz, université Stanford, Journal of Experimental Psychology, 2014</div>"),
   s("<h2>Même sur un tapis de marche, face à un mur blanc.</h2><p class='it'>C'est le mouvement qui compte, pas forcément le paysage.</p><div class='src'>Oppezzo &amp; Schwartz, université Stanford, 2014</div>"),
   s("<div class='kicker'>Essaie</div><h2>L'appel en marchant.</h2><p>Pas d'écran à partager&nbsp;? Fais-le dehors.</p>"),
   s("<div class='kicker'>Essaie</div><h2>Le problème qui coince.</h2><p>Pose-le, marche 10 minutes, reviens. Note ce qui a bougé.</p>"),
   cta("Tu réfléchis mieux assis ou en marchant&nbsp;?", "Écris A pour assis, B pour en marchant." + ABO)])

sig = [("Ta semaine est pleine dès le lundi matin.", "Aucune place pour l'imprévu… qui arrive toujours."),
       ("Tes rendez-vous s'enchaînent sans pause.", "Pas une minute pour digérer ce que tu viens de décider."),
       ("Tes priorités passent après 19&nbsp;h.", "Quand tout le monde est parti. Et ton énergie aussi."),
       ("Tu dis oui avant de vérifier.", "Puis tu réorganises tout pour tenir ta parole."),
       ("Aucun créneau n'est réservé pour toi.", "Ni pour réfléchir, ni pour souffler.")]
P(id="c05", slug="2026-10-22_agenda-te-dirige", date="2026-10-22T10:00:00", theme="sauge", pilier="Juste dose",
  title="5 signes que ton agenda te dirige",
  text="5 signes que ton agenda te dirige, et pas l'inverse. Tu en coches plus de 2 ? Oui ou non ?\n\n#organisation #agenda " + H,
  slides=[cover("5 signes que ton agenda te dirige", "Et pas l'inverse.")] + [num(i, a, b) for i, (a, b) in enumerate(sig, 1)] +
   [cta("Tu en coches plus de 2&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c06", slug="2026-10-22_regle-des-2-minutes", date="2026-10-22T18:00:00", theme="marine", pilier="Juste dose",
  title="La règle des 2 minutes",
  text="Moins de 2 minutes ? Fais-le tout de suite. La règle des 2 minutes, pour vider ta tête sans remplir ta journée. Tu l'appliques déjà ? Oui ou non ?\n\n#organisation #productivite " + H,
  slides=[cover("La règle des 2&nbsp;minutes", "Pour vider ta tête sans remplir ta journée."),
   s("<h2>Une tâche prend moins de 2&nbsp;minutes&nbsp;? Fais-la tout de suite.</h2><div class='src'>David Allen, méthode «&nbsp;Getting Things Done&nbsp;», 2001</div>"),
   s("<h2>Pourquoi&nbsp;?</h2><p>La noter, la relire, y repenser… te coûte plus cher que de la faire.</p>"),
   s("<div class='kicker'>Exemples</div><ul><li>Répondre «&nbsp;oui, mardi 14&nbsp;h&nbsp;».</li><li>Classer une facture.</li><li>Envoyer le document promis.</li></ul>"),
   s("<div class='kicker'>Attention</div><h2>2 minutes, pas 20.</h2><p class='it'>Si tu enchaînes les «&nbsp;petites tâches&nbsp;» toute la matinée, ce n'est plus une règle. C'est une fuite.</p>"),
   cta("Tu l'appliques déjà&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c07", slug="2026-10-23_ce-que-dose-ne-sera-pas", date="2026-10-23T10:00:00", theme="creme", pilier="Coulisses",
  title="Ce que DOSE ne sera pas",
  text="Coulisses : avant de te dire ce que DOSE sera, voici ce qu'elle ne sera pas. Tu veux la suite ? Écris « oui » et abonne-toi pour suivre le lancement.\n\n#coulisses #lancement " + H,
  slides=[cover("Ce que DOSE ne sera pas", "", "Coulisses"),
   num(1, "Une méthode pour travailler plus.", "Le but n'est pas d'en faire plus. C'est d'en faire juste assez, au bon moment."),
   num(2, "Des conseils bien-être génériques.", "Elle est pensée pour les dirigeants de TPE&nbsp;: leur réalité, leurs contraintes."),
   num(3, "Une promesse de miracle.", "Pas de raccourci. Des repères concrets, à ton rythme."),
   num(4, "Un truc de plus à caser dans ton agenda.", "Une méthode qui t'épuise a raté sa cible."),
   cta("Tu veux savoir ce qu'elle sera&nbsp;?", "Écris «&nbsp;oui&nbsp;» en commentaire.<br>Et abonne-toi pour suivre le lancement.")])

P(id="c08", slug="2026-10-23_mails-a-ou-b", date="2026-10-23T18:00:00", theme="sauge", pilier="Juste dose",
  title="Tes mails : A ou B ?",
  text="Boîte mail ouverte toute la journée ou 2 à 3 créneaux par jour ? Tu es plutôt A ou B ? Écris-le en commentaire.\n\n#organisation #mails " + H,
  slides=[cover("Tes mails&nbsp;: A ou&nbsp;B&nbsp;?", "Sois honnête."),
   s("<div class='kicker'>Profil A</div><h2>Boîte ouverte toute la journée.</h2><ul><li>Tu réponds dans la minute.</li><li>Chaque notification t'interrompt.</li><li>Le soir, tu ne sais plus ce que tu as fait.</li></ul>"),
   s("<div class='kicker'>Profil B</div><h2>2 ou 3 créneaux par jour.</h2><ul><li>Tu traites tes mails par lots.</li><li>Notifications coupées le reste du temps.</li><li>Tes vraies priorités passent avant.</li></ul>"),
   s("<h2>Ta boîte mail, c'est la to-do des autres.</h2><p class='it'>Ce sont leurs priorités qui arrivent. Pas forcément les tiennes.</p>"),
   s("<div class='kicker'>À tester demain</div><h2>Ouvre tes mails après ta première priorité.</h2><p>Pas avant. Et observe ce qui change.</p>"),
   cta("Tu es plutôt A ou&nbsp;B&nbsp;?", "Écris A ou B en commentaire." + ABO)])

P(id="c09", slug="2026-10-24_dormir-moins", date="2026-10-24T10:00:00", theme="marine", pilier="Dose de réalité",
  title="Dormir moins pour en faire plus ?",
  text="Dormir moins pour en faire plus ? Après 17 à 19 heures sans dormir, certaines performances baissent autant qu'avec 0,5 g/l d'alcool. Tu as déjà pris une décision importante à minuit ? Oui ou non ?\n\n#sommeil #santedudirigeant " + H,
  slides=[cover("Dormir moins pour en faire plus&nbsp;?", "", "Dose de réalité"),
   s("<div class='big'>17&nbsp;h</div><p>Après 17 à 19 heures sans dormir, certaines performances baissent autant qu'avec 0,5&nbsp;g d'alcool par litre de sang.</p><div class='src'>Williamson &amp; Feyer, Occupational and Environmental Medicine, 2000</div>"),
   s("<h2>0,5&nbsp;g/l, c'est la limite légale pour conduire en France.</h2><div class='src'>Code de la route, article R234-1</div>"),
   s("<h2>Debout à 6&nbsp;h, dernier mail à 23&nbsp;h.</h2><p class='it'>Ça fait 17 heures. Et tu prends encore des décisions.</p>"),
   s("<h2>Ton sommeil n'est pas du temps perdu.</h2><p>C'est du temps de récupération pour celui ou celle qui pilote l'entreprise.</p>"),
   s("<div class='kicker'>Le repère</div><h2>Tes décisions importantes&nbsp;? Pas après 22&nbsp;h.</h2><p class='it'>Elles peuvent presque toujours attendre le lendemain matin.</p>"),
   cta("Une décision importante à minuit, ça t'est déjà arrivé&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c10", slug="2026-10-24_couper-le-week-end", date="2026-10-24T18:00:00", theme="creme", pilier="Énergie du dirigeant",
  title="Ce week-end, tu coupes vraiment ?",
  text="31 % des dirigeants de TPE n'ont pris aucun congé cet été. Alors ce week-end, on commence petit : 3 façons de couper pour de vrai. Tu coupes ce week-end ? Oui ou non ?\n\n#equilibre #weekend " + H,
  slides=[cover("Ce week&#8209;end, tu coupes vraiment&nbsp;?", "3 façons de décrocher pour de vrai."),
   s("<div class='big'>31&nbsp;%</div><p>des dirigeants de TPE n'ont pris aucun congé cet été.</p><div class='src'>Baromètre des TPE Ifop / Fiducial, juillet 2026</div>"),
   num(1, "Ferme la boucle vendredi.", "Note les 3 sujets en cours. Ta tête n'a plus besoin de les retenir."),
   num(2, "Range ton téléphone pro.", "Pas juste en silencieux. Hors de vue."),
   num(3, "Fais quelque chose avec tes mains.", "Cuisiner, jardiner, bricoler, bouger&nbsp;: ton cerveau change enfin de sujet."),
   cta("Tu coupes ce week&#8209;end&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c11", slug="2026-10-26_piloter-ou-subir", date="2026-10-26T10:00:00", theme="sauge", pilier="Juste dose",
  title="Ta semaine : tu la pilotes ou tu la subis ?",
  text="C'est lundi : 3 questions pour savoir si tu pilotes ta semaine ou si tu la subis. Écris 1 si tu pilotes, 2 si tu subis.\n\n#organisation #lundi " + H,
  slides=[cover("Ta semaine&nbsp;: tu la pilotes ou tu la subis&nbsp;?", "3 questions pour le savoir."),
   s("<div class='kicker'>Question 1</div><h2>Tu connais tes 3 priorités de la semaine&nbsp;?</h2>"),
   s("<div class='kicker'>Question 2</div><h2>Tu as bloqué un créneau pour avancer sans interruption&nbsp;?</h2>"),
   s("<div class='kicker'>Question 3</div><h2>Tu sais déjà à quelle heure tu t'arrêtes ce soir&nbsp;?</h2>"),
   s("<h2>2 ou 3 oui&nbsp;: tu pilotes.</h2><p class='it'>0 ou 1&nbsp;: ta semaine risque de décider pour toi. Bonne nouvelle, c'est lundi. Il est encore temps.</p>"),
   cta("Tu pilotes ou tu subis&nbsp;?", "Écris 1 si tu pilotes, 2 si tu subis." + ABO)])

P(id="c12", slug="2026-10-26_patron-ne-sarrete-jamais", date="2026-10-26T18:00:00", theme="marine", pilier="Dose de réalité",
  title="Un vrai patron ne s'arrête jamais ?",
  text="Un vrai patron ne s'arrête jamais ? 42 % des dirigeants de TPE-PME ont déjà continué à travailler alors qu'ils pensaient devoir s'arrêter. Ta boîte tiendrait une semaine sans toi ? Oui ou non ?\n\n#santedudirigeant #delegation " + H,
  slides=[cover("Un vrai patron ne s'arrête jamais&nbsp;?", "", "Dose de réalité"),
   s(f"<div class='big'>42&nbsp;%</div><p>des dirigeants de TPE-PME ont déjà continué à travailler alors qu'ils pensaient avoir besoin de s'arrêter.</p><div class='src'>{AG2R}</div>"),
   s(f"<div class='big'>56&nbsp;%</div><p>estiment qu'un arrêt de quelques jours aurait des conséquences pour leur entreprise.</p><div class='src'>{AG2R}</div>"),
   s(f"<div class='big'>46&nbsp;%</div><p>de ceux qui ne s'arrêtent pas invoquent la même raison&nbsp;: personne ne peut les remplacer.</p><div class='src'>{AG2R}</div>"),
   s("<h2>Le problème n'est pas de s'arrêter.</h2><p class='it'>C'est d'avoir une entreprise qui ne le supporte pas. Et ça, ça se construit.</p>"),
   cta("Ta boîte tiendrait une semaine sans toi&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

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
