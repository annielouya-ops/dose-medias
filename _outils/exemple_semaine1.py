import json, subprocess, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render.py")
G = "<p class='src' style='font-size:30px;margin-top:40px'>Glisse &rarr;</p>"
def cover(h1, sub="", kicker=""):
    k = f"<div class='kicker'>{kicker}</div>" if kicker else ""
    s = f"<div class='rule'></div><p class='it'>{sub}</p>" if sub else ""
    return {"cls": "center", "nofoot": True, "html": "{DROP_L}" + k + f"<h1>{h1}</h1>" + s + G}
def cta(h2, p):
    return {"cls": "center", "nofoot": True, "html": "{DROP_L}" + f"<h2>{h2}</h2><div class='rule'></div><p>{p}</p>"}
def s(html): return {"html": html}

posts = []

posts.append(dict(id="c02", slug="2026-10-13_paradoxe-dirigeant", date="2026-10-13T18:00:00", theme="sauge",
 title="« Ça va. » Vraiment ?",
 text="86 % des dirigeants disent que ça va. 64 % vivent pourtant des périodes de stress intense. Et toi, combien de « oui » aux 3 questions ?\n\n#santedudirigeant #entrepreneur #chefdentreprise #stress #justedose",
 slides=[cover("« Ça va. »", "Le paradoxe du dirigeant.", "Vraiment ?"),
  s("<div class='big'>86&nbsp;%</div><p>des dirigeants de TPE et PME se disent en bonne santé mentale.</p><div class='src'>Baromètre AG2R La Mondiale / Ipsos bva, septembre 2026</div>"),
  s("<div class='big'>64&nbsp;%</div><p>vivent pourtant des périodes de stress intense au travail.</p><div class='src'>Baromètre AG2R La Mondiale / Ipsos bva, septembre 2026</div>"),
  s("<h2>Le problème n'est pas le stress.</h2><p class='it'>C'est de ne plus le voir.</p>"),
  s("<div class='kicker'>3 questions honnêtes</div><ul><li>Tu dors d'une traite&nbsp;?</li><li>Tu as eu une vraie journée off ce mois-ci&nbsp;?</li><li>Tu sais ce qui te vide le plus&nbsp;?</li></ul>"),
  cta("Combien de «&nbsp;oui&nbsp;»&nbsp;?", "Dis-le-moi en commentaire.<br>Et abonne-toi : la juste dose arrive bientôt.")]))

sig = [("Tu te réveilles en pensant déjà à ta to-do.", "Ton cerveau n'a pas vraiment coupé."),
       ("Tu repousses les décisions importantes.", "Trop de petites décisions usent ta capacité à trancher."),
       ("Tu n'as plus de temps pour ce qui t'a fait entreprendre.", "L'urgent a mangé l'essentiel."),
       ("Ton week-end ressemble à une journée de bureau plus calme.", "Sans vraie coupure, pas de vraie récupération."),
       ("Tu t'agaces pour des détails.", "L'irritabilité est souvent le premier signal de fatigue.")]
posts.append(dict(id="c03", slug="2026-10-14_5-signaux", date="2026-10-14T10:00:00", theme="sauge",
 title="5 signaux que tu dépasses ta juste dose",
 text="5 signaux que tu dépasses ta juste dose. Tu en coches combien ? Dis-le en commentaire.\n\n#entrepreneur #chefdentreprise #burnoutentrepreneur #santedudirigeant #justedose",
 slides=[cover("5 signaux que tu dépasses ta juste dose", "Sois honnête avec toi-même.")] +
  [s(f"<div class='num'>0{i}</div><h2>{a}</h2><p class='it'>{b}</p>") for i, (a, b) in enumerate(sig, 1)] +
  [cta("Tu en coches combien&nbsp;?", "Dis-le en commentaire.<br>Et abonne-toi pour la suite.")]))

posts.append(dict(id="c04", slug="2026-10-14_regle-des-3", date="2026-10-14T18:00:00", theme="marine",
 title="Prioriser sans culpabiliser",
 text="Ta to-do fait 27 lignes, ta journée 8 heures. La règle des 3 priorités pour avancer sans culpabiliser. Quelles sont les tiennes cette semaine ?\n\n#entrepreneur #organisation #productivite #chefdentreprise #justedose",
 slides=[cover("Prioriser sans culpabiliser", "La règle des 3 priorités."),
  s("<h2>Ta to-do fait 27 lignes. Ta journée, 8 heures.</h2><p class='it'>Le problème n'est pas toi. C'est la liste.</p>"),
  s("<div class='kicker'>Étape 1</div><h2>Choisis 3 priorités, pas 10.</h2><p>Celles qui font vraiment avancer ton entreprise cette semaine.</p>"),
  s("<div class='kicker'>Étape 2</div><h2>Fais-les en premier.</h2><p>Avant les mails. Avant les urgences des autres.</p>"),
  s("<div class='kicker'>Étape 3</div><h2>Le reste attend. Et c'est <span class='accent'>OK</span>.</h2><p>Ce que tu ne fais pas aujourd'hui n'est pas un échec. C'est un choix.</p>"),
  cta("Tes 3 priorités de la semaine&nbsp;?", "Écris-les en commentaire.<br>Et abonne-toi pour la suite.")]))

posts.append(dict(id="c05", slug="2026-10-15_matin-ou-soir", date="2026-10-15T18:00:00", theme="sauge",
 title="Matin ou soir ?",
 text="Une heure à 9 h ne vaut pas une heure à 16 h. Travaille avec ton rythme, pas contre lui. Tu es plutôt matin ou soir ?\n\n#entrepreneur #energie #organisation #chefdentreprise #justedose",
 slides=[cover("Matin ou soir&nbsp;?", "Travaille avec ton rythme, pas contre lui."),
  s("<h2>Une heure à 9&nbsp;h ne vaut pas une heure à 16&nbsp;h.</h2><p>Ton énergie varie au fil de la journée. Ton agenda, lui, fait comme si de rien n'était.</p>"),
  s("<div class='num'>01</div><h2>Repère tes pics.</h2><p>Pendant une semaine, note les moments où tu es le plus concentré·e.</p>"),
  s("<div class='num'>02</div><h2>Protège-les.</h2><p>Place-y tes tâches les plus exigeantes : stratégie, écriture, décisions.</p>"),
  s("<div class='num'>03</div><h2>Range l'administratif dans tes creux.</h2><p>Mails, factures, relances : ils n'ont pas besoin de ton meilleur cerveau.</p>"),
  cta("Tu es plutôt matin ou soir&nbsp;?", "Dis-le-moi en commentaire.")]))

posts.append(dict(id="c06", slug="2026-10-16_travailler-plus", date="2026-10-16T10:00:00", theme="marine",
 title="Travailler plus pour réussir plus ?",
 text="Travailler plus pour réussir plus ? Les chiffres disent autre chose. Combien d'heures as-tu travaillé cette semaine ?\n\n#entrepreneur #hustleculture #chefdentreprise #santedudirigeant #justedose",
 slides=[cover("Travailler plus pour réussir plus&nbsp;?", "", "Dose de réalité"),
  s("<h2>Au-delà de 50 heures par semaine, la productivité par heure chute nettement.</h2><div class='src'>Étude de l'économiste John Pencavel, Stanford, 2014</div>"),
  s("<h2>70 heures de travail ne produisent guère plus que 55.</h2><p class='it'>Les heures en plus ? Surtout de la fatigue.</p><div class='src'>Étude de l'économiste John Pencavel, Stanford, 2014</div>"),
  s("<div class='big'>49&nbsp;%</div><p>des dirigeants ont des troubles du sommeil.</p><div class='src'>Baromètre Fondation MMA / Ifop, 2026</div>"),
  s("<h2>Un dirigeant épuisé décide moins bien.</h2><p class='it'>Le repos n'est pas une récompense. C'est un outil de pilotage.</p>"),
  cta("Combien d'heures cette semaine&nbsp;?", "Sois honnête, en commentaire.<br>Et abonne-toi : la juste dose arrive bientôt.")]))

days = [("Lundi", "Choisis tes 3 priorités.", "15 minutes pour décider ce qui compte vraiment."),
        ("Chaque jour", "Deux blocs de concentration.", "90 minutes sans téléphone ni mails."),
        ("Mercredi", "Une demi-journée sans rendez-vous.", "Pour réfléchir à ton entreprise, pas seulement y travailler."),
        ("Vendredi", "La revue de semaine.", "Ce qui a avancé, ce qui t'a vidé, ce que tu changes."),
        ("Week-end", "Une vraie coupure.", "Au moins une journée entière. Ton énergie de lundi en dépend.")]
posts.append(dict(id="c07", slug="2026-10-17_semaine-juste-dose", date="2026-10-17T10:00:00", theme="marine",
 title="Une semaine en juste dose",
 text="5 repères simples pour une semaine de dirigeant en juste dose. Lequel appliques-tu déjà ?\n\n#entrepreneur #organisation #chefdentreprise #tpe #justedose",
 slides=[cover("Une semaine en juste dose", "5 repères simples pour dirigeant·e de TPE.")] +
  [s(f"<div class='kicker'>{d}</div><h2>{a}</h2><p>{b}</p>") for d, a, b in days] +
  [cta("Lequel appliques-tu déjà&nbsp;?", "Dis-le-moi en commentaire.<br>Et abonne-toi pour la suite.")]))

posts.append(dict(id="c08", slug="2026-10-17_coulisses-construire-dose", date="2026-10-17T18:00:00", theme="creme",
 title="Ce que construire DOSE m'apprend",
 text="Coulisses : ce que la construction de DOSE m'apprend. La suite arrive bientôt, abonne-toi pour suivre le lancement.\n\n#coulisses #entrepreneure #lancement #formation #justedose",
 slides=[cover("Ce que construire DOSE m'apprend", "", "Coulisses"),
  s("<div class='num'>01</div><h2>Appliquer ma propre méthode.</h2><p class='it'>Construire une méthode anti-épuisement en s'épuisant&nbsp;? Non merci.</p>"),
  s("<div class='num'>02</div><h2>Déléguer ce qui n'est pas mon cœur de métier.</h2><p class='it'>Une partie des outils a été confiée à une freelance. Du temps gagné pour l'essentiel.</p>"),
  s("<div class='num'>03</div><h2>Tout écrire avant de tout produire.</h2><p class='it'>Les cinq modules ont d'abord été entièrement scénarisés.</p>"),
  s("<div class='num'>04</div><h2>Avancer à la <span class='accent'>juste dose</span>.</h2><p class='it'>Pas tout en même temps. Une étape, puis la suivante.</p>"),
  cta("La suite des coulisses arrive.", "Abonne-toi pour suivre le lancement.")]))

videos = [
 dict(id="v01", slug="2026-10-15_pourquoi-dose", date="2026-10-15T10:00:00", theme="creme",
  title="Je lance une méthode",
  text="Je lance une méthode pour entreprendre sans s'épuiser. Voici pourquoi. Abonne-toi pour suivre le lancement.\n\n#coulisses #entrepreneur #lancement #santedudirigeant #justedose",
  frames=["<div class='kicker'>Coulisses</div><h1>Je lance une méthode.</h1>",
          "<h2>Pour entreprendre <span class='accent'>sans s'épuiser</span>.</h2>",
          "<h2>Pourquoi&nbsp;?</h2><p class='it'>Parce que trop de dirigeants brillants s'usent à force de tout porter seuls.</p>",
          "{DROP_L}<h2>DOSE arrive bientôt.</h2><p>Abonne-toi pour suivre le lancement.</p>"]),
 dict(id="v02", slug="2026-10-16_dernier-jour-off", date="2026-10-16T18:00:00", theme="sauge",
  title="Ton dernier vrai jour off ?",
  text="À quand remonte ton dernier vrai jour off ? Réponds en commentaire, sans tricher.\n\n#entrepreneur #santedudirigeant #equilibre #chefdentreprise #justedose",
  frames=["<h1>À quand remonte ton dernier vrai jour off&nbsp;?</h1>",
          "<h2>Sans mails.<br>Sans «&nbsp;juste un petit appel&nbsp;».</h2>",
          "<h2>Si tu dois réfléchir plus de 5 secondes…</h2>",
          "<h2>…il est peut-être temps d'en poser un.</h2><p>Dis-le-moi en commentaire.</p>"]),
]

os.makedirs("specs", exist_ok=True)
for p in posts:
    f = f"specs/{p['id']}.json"
    json.dump({"theme": p["theme"], "slides": p["slides"]}, open(f, "w"), ensure_ascii=False)
    subprocess.run(["python3", "-I", R, f, f"out/{p['id']}"], check=True)
for v in videos:
    f = f"specs/{v['id']}.json"
    json.dump({"theme": v["theme"], "nonum": True, "slides": [{"cls": "center", "html": h} for h in v["frames"]]}, open(f, "w"), ensure_ascii=False)
    subprocess.run(["python3", "-I", R, f, f"out/{v['id']}"], check=True)
json.dump({"posts": [{k: p[k] for k in ("id", "slug", "date", "title", "text")} | {"n": len(p["slides"])} for p in posts],
           "videos": [{k: v[k] for k in ("id", "slug", "date", "title", "text")} | {"n": len(v["frames"])} for v in videos]},
          open("semaine1_posts.json", "w"), ensure_ascii=False, indent=1)
print("done")
