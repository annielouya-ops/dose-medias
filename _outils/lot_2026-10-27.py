"""Lot semaine 3 : carrousels du mardi 27 octobre au lundi 2 novembre 2026.
Usage : python3 lot_2026-10-27.py <dossier_de_travail> [ids...]
Rotation : dernier post daté = marine (lundi 26, 18 h) -> on repart sur crème.
Piliers : Juste dose 4, Énergie 3, Dose de réalité 3, Coulisses 2.
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
ALB = "Albulescu et al., PLOS ONE, 2022 (synthèse de 22 études)"
BUE = "Buehler, Griffin &amp; Ross, Journal of Personality and Social Psychology, 1994"

posts = []
P = lambda **k: posts.append(k)

# Mardi 27
P(id="c01", slug="2026-10-27_pauses-temps-perdu", date="2026-10-27T10:00:00", theme="creme", pilier="Énergie du dirigeant",
  title="Tes pauses, du temps perdu ?",
  text="Tu culpabilises de faire une pause ? Une synthèse de 22 études montre que les micro-pauses de moins de 10 minutes redonnent de l'énergie et réduisent la fatigue. Tu en fais dans ta journée ? Oui ou non ?\n\n#energie #pause " + H,
  slides=[cover("Tes pauses, du temps perdu&nbsp;?", "Ce que disent 22 études."),
   s(f"<div class='big'>10&nbsp;min</div><p>Une micro-pause, c'est moins de 10 minutes loin de ta tâche.</p><div class='src'>{ALB}</div>"),
   s(f"<h2>Résultat&nbsp;: plus d'énergie, moins de fatigue.</h2><p class='it'>C'est le constat de la synthèse, toutes études confondues.</p><div class='src'>{ALB}</div>"),
   s(f"<h2>Pour les tâches lourdes, une pause plus longue.</h2><p>Une micro-pause recharge. Elle ne remplace pas une vraie coupure.</p><div class='src'>{ALB}</div>"),
   s("<div class='kicker'>À tester demain</div><ul><li>Te lever entre deux rendez-vous.</li><li>Regarder par la fenêtre, pas ton téléphone.</li><li>Marcher 5 minutes après une décision difficile.</li></ul>"),
   cta("Tu fais des pauses dans ta journée&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c02", slug="2026-10-27_goulot-de-ta-boite", date="2026-10-27T18:00:00", theme="sauge", pilier="Juste dose",
  title="5 signes que tout passe par toi",
  text="5 signes que tu es devenu le goulot de ta propre boîte. Tu en coches plus de 2 ? Oui ou non ?\n\n#delegation #organisation " + H,
  slides=[cover("5 signes que tout passe par toi", "Et que ta boîte t'attend pour avancer.")] +
   [num(i, a, b) for i, (a, b) in enumerate([
     ("Ton équipe attend ta validation pour tout.", "Même pour les petites décisions."),
     ("Tu es en copie de tous les mails.", "«&nbsp;Au cas où.&nbsp;»"),
     ("Les dossiers s'empilent quand tu es absent.", "Et t'attendent sagement à ton retour."),
     ("Tu refais le travail des autres.", "Plus vite, plus simple… et toujours toi."),
     ("Tu es le seul à avoir les mots de passe.", "Et la mémoire de tout."),
   ], 1)] + [cta("Tu en coches plus de 2&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Mercredi 28
P(id="c03", slug="2026-10-28_urgent-ou-important", date="2026-10-28T10:00:00", theme="marine", pilier="Juste dose",
  title="Urgent ou important ?",
  text="Urgent ne veut pas dire important. La matrice d'Eisenhower en 4 cases pour trier ta journée. Ta journée d'hier, c'était plutôt A (urgent) ou B (important) ?\n\n#organisation #priorites " + H,
  slides=[cover("Urgent ou important&nbsp;?", "La matrice qui trie ta journée en 4 cases."),
   s("<h2>«&nbsp;Ce qui est important est rarement urgent, et ce qui est urgent est rarement important.&nbsp;»</h2><div class='src'>Dwight D. Eisenhower, discours de 1954, idée reprise par Stephen Covey (1989)</div>"),
   s("<div class='kicker'>Case 1 · Urgent et important</div><h2>Fais-le.</h2><p>Une vraie crise, une échéance client. Maintenant.</p>"),
   s("<div class='kicker'>Case 2 · Important, pas urgent</div><h2>Planifie-le.</h2><p>Stratégie, recrutement, ta santé. C'est ici que ton entreprise se construit.</p>"),
   s("<div class='kicker'>Cases 3 et 4</div><h2>Urgent mais pas important&nbsp;? Délègue.</h2><p>Ni l'un ni l'autre&nbsp;? Supprime.</p>"),
   s("<h2>Le piège&nbsp;: vivre dans la case 1.</h2><p class='it'>Chaque urgence gérée donne l'impression d'avancer. La case 2, elle, attend toujours.</p>"),
   cta("Hier, plutôt A ou&nbsp;B&nbsp;?", "A = surtout de l'urgent.<br>B = surtout de l'important." + ABO)])

P(id="c04", slug="2026-10-28_cest-toi-qui-choisis", date="2026-10-28T18:00:00", theme="creme", pilier="Coulisses",
  title="Coulisses : c'est toi qui choisis",
  text="Coulisses : le prochain carrousel, c'est toi qui le choisis. 1 = déléguer sans tout perdre, 2 = dormir quand ta tête ne s'arrête pas. Écris 1 ou 2 en commentaire.\n\n#coulisses #lancement " + H,
  slides=[cover("C'est toi qui choisis.", "Le prochain sujet se décide en commentaire.", "Coulisses"),
   s("<h2>DOSE se construit pour les dirigeants de TPE.</h2><p class='it'>Alors autant te demander ce qui t'aide vraiment.</p>"),
   s("<div class='num'>1</div><h2>Déléguer sans tout perdre.</h2><p class='it'>Lâcher une tâche sans perdre le contrôle de ta boîte.</p>"),
   s("<div class='num'>2</div><h2>Dormir quand ta tête ne s'arrête pas.</h2><p class='it'>Couper le soir, même quand les dossiers continuent de tourner.</p>"),
   s("<h2>Le sujet qui gagne sort la semaine prochaine.</h2><p>Promis.</p>"),
   cta("Tu votes 1 ou 2&nbsp;?", "Écris 1 ou 2 en commentaire.<br>Et abonne-toi pour suivre le lancement.")])

# Jeudi 29
P(id="c05", slug="2026-10-29_voleurs-energie", date="2026-10-29T10:00:00", theme="sauge", pilier="Énergie du dirigeant",
  title="4 voleurs d'énergie du dirigeant",
  text="4 voleurs d'énergie que presque tous les dirigeants connaissent. Lequel te coûte le plus ? Écris 1, 2, 3 ou 4.\n\n#energie #santedudirigeant " + H,
  slides=[cover("4 voleurs d'énergie du dirigeant", "Tu en reconnais combien&nbsp;?"),
   s(f"<div class='num'>01</div><h2>Les échéances qui s'empilent.</h2><p class='it'>52&nbsp;% des dirigeants de TPE-PME citent les échéances accumulées et les urgences comme source de stress.</p><div class='src'>{AG2R}</div>"),
   num(2, "Les décisions en série.", "Chaque petit choix grignote ta capacité à bien trancher les grands."),
   num(3, "Les interruptions.", "Un appel, une notification, une question «&nbsp;rapide&nbsp;». Et ta concentration repart à zéro."),
   num(4, "Les «&nbsp;oui&nbsp;» réflexes.", "Chaque oui donné trop vite, c'est du temps pris sur tes priorités."),
   s("<h2>Tu ne les supprimeras pas tous.</h2><p class='it'>Mais tu peux choisir celui que tu attaques en premier.</p>"),
   cta("Lequel te coûte le plus&nbsp;?", "Écris 1, 2, 3 ou 4 en commentaire." + ABO)])

P(id="c06", slug="2026-10-29_loi-de-parkinson", date="2026-10-29T18:00:00", theme="marine", pilier="Dose de réalité",
  title="Plus de temps = meilleur travail ?",
  text="Plus tu te donnes de temps, mieux c'est fait ? La loi de Parkinson dit l'inverse : le travail s'étale pour remplir le temps disponible. Tu te fixes des délais courts ? Oui ou non ?\n\n#productivite #organisation " + H,
  slides=[cover("Plus de temps = meilleur travail&nbsp;?", "", "Dose de réalité"),
   s("<h2>«&nbsp;Le travail s'étale de façon à occuper tout le temps disponible pour son achèvement.&nbsp;»</h2><div class='src'>Cyril Northcote Parkinson, The Economist, 1955</div>"),
   s("<h2>Une journée pour un devis&nbsp;?</h2><p class='it'>Il prendra la journée. Une heure&nbsp;? Il prendra souvent une heure.</p>"),
   s("<div class='kicker'>Essaie</div><h2>Donne une durée à chaque tâche.</h2><p>Pas juste une date. Une durée&nbsp;: 45 minutes, pas «&nbsp;jeudi&nbsp;».</p>"),
   s("<div class='kicker'>Attention</div><h2>Court, pas impossible.</h2><p class='it'>Un délai serré te concentre. Un délai irréaliste t'épuise.</p>"),
   cta("Tu te fixes des délais courts&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Vendredi 30
P(id="c07", slug="2026-10-30_fermer-ta-journee", date="2026-10-30T10:00:00", theme="creme", pilier="Énergie du dirigeant",
  title="Ferme ta journée avant de partir",
  text="Tes dossiers te suivent jusqu'au lit ? Écrire un plan pour ce qui n'est pas fini aide ta tête à lâcher prise. Tu as un rituel pour fermer ta journée ? Oui ou non ?\n\n#energie #equilibre " + H,
  slides=[cover("Ferme ta journée avant de partir.", "Pour que tes dossiers ne te suivent pas jusqu'au lit."),
   s("<h2>Une tâche pas finie continue de tourner dans ta tête.</h2><p class='it'>Elle revient pendant que tu fais autre chose.</p><div class='src'>Masicampo &amp; Baumeister, Journal of Personality and Social Psychology, 2011</div>"),
   s("<h2>Écrire un plan précis pour cette tâche suffit à calmer ces pensées.</h2><p>Même sans l'avoir terminée.</p><div class='src'>Masicampo &amp; Baumeister, Journal of Personality and Social Psychology, 2011</div>"),
   s("<div class='kicker'>Le rituel en 5 minutes</div><ul><li>Note ce qui reste en cours.</li><li>Pour chaque sujet&nbsp;: la prochaine action et quand.</li><li>Ferme l'ordinateur. Pour de bon.</li></ul>"),
   s("<h2>Ta tête n'a plus besoin de retenir.</h2><p class='it'>C'est écrit. Elle peut passer à autre chose.</p>"),
   cta("Tu as un rituel pour fermer ta journée&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c08", slug="2026-10-30_dire-non", date="2026-10-30T18:00:00", theme="sauge", pilier="Juste dose",
  title="4 phrases pour dire non sans te justifier",
  text="Dire non sans te justifier pendant 10 minutes : 4 phrases simples à garder sous la main. Tu as du mal à dire non ? Oui ou non ?\n\n#organisation #limites " + H,
  slides=[cover("4 phrases pour dire non sans te justifier", "Garde-les sous la main."),
   num(1, "«&nbsp;Pas cette semaine. On en reparle lundi&nbsp;?&nbsp;»", "Tu ne refuses pas. Tu choisis le moment."),
   num(2, "«&nbsp;Si je dis oui, qu'est-ce que je retire&nbsp;?&nbsp;»", "Ton agenda n'est pas extensible. Rends le choix visible."),
   num(3, "«&nbsp;Je ne suis pas la bonne personne. Voici qui l'est.&nbsp;»", "Un non utile, avec une solution."),
   num(4, "«&nbsp;Non, merci.&nbsp;»", "Une phrase complète. Pas besoin d'en rajouter."),
   s("<h2>Chaque oui de trop est un non à tes priorités.</h2><p class='it'>Choisis lequel tu dis.</p>"),
   cta("Tu as du mal à dire non&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

# Samedi 31
P(id="c09", slug="2026-10-31_dirigeant-gere-seul", date="2026-10-31T10:00:00", theme="marine", pilier="Dose de réalité",
  title="Un dirigeant, ça gère seul ?",
  text="Un dirigeant, ça gère seul ? 39 % des dirigeants de TPE-PME disent que la solitude est un problème pour eux. Tu as quelqu'un avec qui parler de tes décisions ? Oui ou non ?\n\n#solitudedudirigeant #santedudirigeant " + H,
  slides=[cover("Un dirigeant, ça gère seul&nbsp;?", "", "Dose de réalité"),
   s(f"<div class='big'>39&nbsp;%</div><p>des dirigeants de TPE-PME disent que la solitude est un problème pour eux, souvent ou de temps en temps.</p><div class='src'>{AG2R}</div>"),
   s(f"<div class='big'>41&nbsp;%</div><p>estiment que leur statut de dirigeant, à lui seul, les freine pour parler de leurs difficultés.</p><div class='src'>{AG2R}</div>"),
   s("<h2>Tout porter seul n'est pas une preuve de force.</h2><p class='it'>C'est souvent un manque d'espace pour en parler.</p>"),
   s("<div class='kicker'>Pistes simples</div><ul><li>Un pair dirigeant à appeler une fois par mois.</li><li>Un club ou un réseau d'entrepreneurs.</li><li>Un mentor qui a déjà vécu ta situation.</li></ul>"),
   cta("Tu as quelqu'un avec qui parler de tes décisions&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c10", slug="2026-10-31_dose-en-3-mots", date="2026-10-31T18:00:00", theme="creme", pilier="Coulisses",
  title="DOSE en 3 mots",
  text="Coulisses : DOSE en 3 mots, pour comprendre ce qui se prépare. Tu veux la suite ? Écris « oui » et abonne-toi pour suivre le lancement.\n\n#coulisses #lancement " + H,
  slides=[cover("DOSE en 3 mots", "Pour comprendre ce qui se prépare.", "Coulisses"),
   num(1, "Juste.", "Pas plus. Pas moins. La juste dose de travail, au bon moment."),
   num(2, "Énergie.", "Ta ressource n°1 de dirigeant. Celle que personne ne pilote à ta place."),
   num(3, "Durer.", "Entreprendre longtemps, pas juste tenir jusqu'aux prochaines vacances."),
   s("<h2>Une méthode pensée pour les dirigeants de TPE.</h2><p class='it'>La suite arrive bientôt.</p>"),
   cta("Tu veux la suite&nbsp;?", "Écris «&nbsp;oui&nbsp;» en commentaire.<br>Et abonne-toi pour suivre le lancement.")])

# Lundi 2 novembre
P(id="c11", slug="2026-11-02_to-do-irrealiste", date="2026-11-02T10:00:00", theme="sauge", pilier="Juste dose",
  title="Ta to-do est-elle réaliste ?",
  text="On sous-estime presque toujours le temps que prend une tâche : en moyenne 34 jours prévus, 56 jours réels dans une étude célèbre. 4 signes que ta to-do de la semaine est irréaliste. Tu en coches au moins 1 ? Oui ou non ?\n\n#organisation #lundi " + H,
  slides=[cover("Ta to-do de la semaine est-elle réaliste&nbsp;?", "Spoiler&nbsp;: probablement pas."),
   s(f"<div class='big' style='font-size:190px;white-space:nowrap'>34 → 56</div><p>Des étudiants prévoyaient 34 jours en moyenne pour finir leur mémoire. Il leur en a fallu 56.</p><div class='src'>{BUE}</div>"),
   num(1, "Tu as reporté les mêmes tâches 3 semaines de suite.", "Elles ne sont pas en retard. Elles sont mal estimées."),
   num(2, "Aucune tâche n'a de durée.", "Juste une liste. Donc aucune limite."),
   num(3, "Ta liste ne laisse aucune place à l'imprévu.", "Alors qu'il arrive chaque semaine."),
   num(4, "Tu comptes sur une «&nbsp;bonne journée&nbsp;».", "Celle où rien ne déraille. Elle n'arrive presque jamais."),
   cta("Tu en coches au moins 1&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

P(id="c12", slug="2026-11-02_tout-est-important", date="2026-11-02T18:00:00", theme="marine", pilier="Dose de réalité",
  title="Tout est important ?",
  text="Tout est important ? Le principe 80/20 dit qu'une petite partie de tes actions produit l'essentiel de tes résultats. Tu sais quelles sont tes 20 % ? Oui ou non ?\n\n#priorites #productivite " + H,
  slides=[cover("Tout est important&nbsp;?", "", "Dose de réalité"),
   s("<div class='big'>80/20</div><p>Une petite partie des causes produit souvent l'essentiel des effets.</p><div class='src'>Principe de Pareto, formulé par Joseph Juran (1951) d'après Vilfredo Pareto (1896)</div>"),
   s("<h2>Ce n'est pas une loi exacte.</h2><p class='it'>C'est un repère. Mais il se vérifie souvent dans une petite entreprise.</p>"),
   s("<div class='kicker'>Exemples à vérifier chez toi</div><ul><li>Quelques clients font l'essentiel de ton chiffre.</li><li>Quelques tâches font avancer ta semaine.</li><li>Quelques personnes prennent l'essentiel de ton énergie.</li></ul>"),
   s("<div class='kicker'>À faire cette semaine</div><h2>Repère tes 20&nbsp;%.</h2><p>Et protège-les avant tout le reste.</p>"),
   cta("Tu sais quelles sont tes 20&nbsp;%&nbsp;?", "Réponds oui ou non en commentaire." + ABO)])

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
