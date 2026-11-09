# Règles éditoriales TikTok DOSE (à appliquer à chaque lot)

Charte éditoriale complète : https://claude.ai/code/artifact/ed81b035-6a03-4526-a1ed-30ec4941923b

## Cadre
- Objectif : 5 000 abonnés fin décembre 2026. Cible : entrepreneurs et dirigeants de TPE.
- 2 posts par jour, 10 h et 18 h (heure de Cayenne, America/Cayenne).
- Phase de TEASING : ne jamais citer le Score DOSE ni le Chronotype DOSE (réservés aux acheteurs). Ne pas dévoiler le contenu de la formation. CTA = « abonne-toi pour suivre le lancement » ou une question.
- TUTOIEMENT obligatoire dans les publications. Ton : exigeant, bienveillant, inspirant, sans jargon.
- Piliers : Juste dose (pédagogie) 35 %, Énergie du dirigeant 25 %, Dose de réalité (idées reçues) 20 %, Coulisses 20 %.
- Pas de conseil médical, pas de promesse de revenus. Chiffres toujours sourcés sur le visuel.
- Tout propos à la première personne d'Annie (coulisses) doit être signalé pour vérification.

## Couleurs
- Marine #002360 = expertise et méthode ; Sauge #7A8B6F = évaluation et progression (auto-questionnements) ;
  Crème #F5F0E6 = inspiration, storytelling, coulisses ; Terracotta #C1653D = réservé aux temps forts du lancement.
- ROTATION OBLIGATOIRE sur la grille : beige(crème) → vert(sauge) → marine → beige… Jamais deux couleurs identiques
  à la suite, trois couleurs différentes sur trois posts consécutifs. Réordonner les contenus plutôt que les recolorer.
- Typo : Montserrat (titres), Fraunces (texte). Polices : télécharger depuis github.com/google/fonts (ofl/montserrat, ofl/fraunces) dans ~/.fonts.

## Chaîne technique
1. Visuels 1080x1920 via _outils/render.py (Playwright + Chromium), un dossier JSON de slides par post (voir exemple_semaine1.py).
2. Vidéos texte : frames PNG + ffmpeg (xfade, piste audio muette).
3. Convertir en JPG qualité 85, déposer dans ce dépôt : AAAA-MM-JJ_slug/01.jpg… ou video.mp4, git push sur main.
4. Metricool (brand id 7389635, fuseau America/Cayenne) : createScheduledPost, provider tiktok, media = URLs
   https://raw.githubusercontent.com/annielouya-ops/dose-medias/main/<dossier>/<fichier>, tiktokData.title obligatoire,
   autoAddMusic true pour les carrousels. Créer en BROUILLON (draft true) : Annie valide avant publication.

## Retour d'expérience semaine 1 (13-17 octobre) — règles ajoutées le 18 octobre
Bilan : 2 136 vues, 32 J'aime, 15 partages, 0 commentaire, 3 abonnés. Meilleurs posts : « DOSE, c'est quoi ? » (548 vues),
« Matin ou soir ? » (288), « 5 signaux » (229), « Travailler plus ? » (225). Pire : vidéo texte muette « Je lance une méthode » (52).
- Plus de vidéos texte muettes : uniquement des carrousels (musique automatique), 10 par semaine.
- Appels à l'action BINAIRES et faciles à commenter : « Tu es plutôt A ou B ? », « Écris 1 ou 2 », « oui ou non ».
  Ne plus poser de questions intimes ou chiffrées (épuisement, heures travaillées) : personne n'y répond en public.
- Privilégier les sujets qui ont marché : choix A/B sur l'organisation, check-lists de signaux, idées reçues chiffrées.
- Face caméra : 2 vidéos par semaine (au lieu de 5), 15 à 20 secondes, filmées au téléphone sans montage, ~20 minutes de tournage.
  Scripts très courts : 1 phrase d'accroche, 2 ou 3 phrases de corps, 1 question binaire de fin. Annie les publie elle-même
  depuis l'application TikTok (son tendance), le dimanche à 10 h et à 18 h. Les créneaux du lundi sont remplis par des carrousels
  préparés dans le lot précédent.
- Le compte TikTok est probablement personnel : portée et taux de visionnage indisponibles dans Metricool. Le rappeler à Annie
  tant que ces données manquent (passage en compte professionnel gratuit dans les réglages TikTok).

## Retour d'expérience semaine 2 (19-26 octobre) — bilan du 26 octobre
Bilan (Metricool, 10 carrousels publiés du 19 au 23) : 2 119 vues (212 par post, contre 178 en semaine 1), 18 J'aime, 5 partages,
0 commentaire, abonnés 3 → 7 (+4, dernier relevé le 22/10). Portée et taux de visionnage toujours indisponibles (compte personnel).
Meilleurs : « La règle des 2 minutes » (360 vues, 5 J'aime), « Tu portes tout seul ? » (320), « 5 signes que ton agenda te dirige » (251).
Pires : « Tes mails : A ou B ? » (55), « Ce que DOSE ne sera pas » (132), « Le multitâche » (167).
INCIDENT : les 2 posts du samedi 24/10 (« Dormir moins », « Couper le week-end ») ont échoué : « You have reached your Metricool account limit »
(plan gratuit, environ 20 posts programmés par mois). Ils restent inédits et réutilisables.
- Leçon : les règles et méthodes nommées et les check-lists « X signes que… » marchent le mieux ; les profils A/B et les coulisses
  « déclaratives » sur DOSE marchent moins bien. Les CTA binaires ne génèrent toujours aucun commentaire : tester un vote qui a une
  conséquence (« c'est toi qui choisis le prochain sujet ») et demander à Annie de répondre elle-même aux premiers commentaires.
- Rythme actuel (+4 abonnés par semaine) très loin de l'objectif de 5 000 fin décembre : il faudra des formats plus viraux
  (face caméra, tendances) et/ou de la promotion, pas seulement plus de carrousels.
- Quota Metricool : 12 posts par semaine dépassent le plan gratuit. Vérifier le quota avant chaque lot.

## Décision du 1er novembre — forfait gratuit Metricool (20 publications par mois)
- Annie reste sur le forfait gratuit : 1 carrousel par jour, du lundi au vendredi à 18 h (environ 20 par mois). Rien le samedi ;
  le dimanche reste réservé aux 2 vidéos face caméra publiées par Annie depuis TikTok (hors Metricool).
- Programmé le 1er/11 (validé par Annie) : 2/11 patron-ne-sarrete-jamais (marine), 3/11 pauses (crème), 4/11 goulot (sauge),
  5/11 urgent-ou-important (marine), 6/11 couper-le-week-end (crème), 9/11 piloter-ou-subir (sauge), 10/11 loi-de-parkinson (marine),
  11/11 c'est-toi-qui-choisis (crème), 12/11 voleurs-energie (sauge), 13/11 dormir-moins (marine). 10 posts sur 20 en novembre.
- En stock, validés, encore en brouillon dans Metricool : fermer-ta-journee et dose-en-3-mots (crème), dire-non et to-do-irrealiste (sauge),
  dirigeant-gere-seul et tout-est-important (marine). Ils couvrent la semaine du 16 au 20/11 (+1). Ne pas recréer de lot de 12 :
  préparer seulement ce qui manque, en tenant compte du quota restant du mois.
- Le vote « C'est toi qui choisis » (11/11) promet le sujet gagnant la semaine suivante : le prévoir dans le lot du 16/11.

## Retour d'expérience semaine 3 (26 octobre - 1er novembre) — bilan du 2 novembre
Bilan : 0 post publié. Dernier post en ligne : 23/10. Les 2 posts du 26/10 ont échoué (quota), le lot du 27/10 est resté en brouillon jusqu'à
la décision du 1er/11. Donc 0 vue, 0 J'aime, 0 partage, 0 commentaire sur la semaine. Abonnés : inconnu, dernier relevé 7 le 22/10.
Cumul des 20 posts du 13 au 23/10 : 4 262 vues (213 par post), 51 J'aime, 21 partages, 0 commentaire. Meilleurs : « DOSE, c'est quoi ? » (548),
« La règle des 2 minutes » (360), « Tu portes tout seul ? » (320). Pires : vidéo muette « Je lance une méthode » (56), « Tes mails : A ou B ? » (55*), « Ce que DOSE ne sera pas » (132*).
- Quota confirmé : 20 posts publiés en octobre, échec dès le 21e (24/10). La limite s'applique à la publication, pas à la création du brouillon.
- ALERTE DONNÉES : Metricool n'a aucune donnée d'évolution du 24/10 au 1er/11, et les vues de chaque post de la semaine 2 sont strictement identiques
  au relevé du 26/10. La synchronisation semble figée depuis le 23/10 environ. *Les chiffres du 23/10 ont sans doute été relevés quelques heures après
  publication : ne pas en conclure que les A/B ou les coulisses échouent. À revérifier dans l'application TikTok.
- Aucune vidéo face caméra n'apparaît dans Metricool (18/10, 25/10, 1er/11) : à confirmer avec Annie (non publiées, ou non remontées).
- Leçon : 10 jours de silence sont le pire scénario pour l'algorithme. Vérifier chaque lundi que le post suivant est bien programmé (draft false),
  pas seulement en brouillon. Pas de nouveau lot sans nouvelles données : attendre les chiffres des posts de novembre avant de produire.
- Lot du 2/11 : aucun carrousel créé (règle du 1er/11). Planning complet jusqu'au 13/11, stock de 6 jusqu'au 23/11. Quota novembre : 10 engagés, 6 en stock,
  4 places libres pour le 24-27/11, dont le sujet gagnant du vote du 11/11.

## Retour d'expérience semaine 4 (2-8 novembre) — bilan du 9 novembre
Publiés (Metricool, statut « Published ») : 5 carrousels à 18 h, du 2 au 6/11 (patron-ne-sarrete-jamais, pauses, goulot, urgent-ou-important,
couper-le-week-end). Le planning a tenu : fin des 10 jours de silence.
Chiffres : AUCUNE donnée dans Metricool pour ces 5 posts (vues, J'aime, partages, commentaires vides) et aucune donnée d'évolution des abonnés
depuis le 22/10 (dernier relevé : 7). La publication fonctionne, mais la synchronisation des statistiques TikTok est bloquée depuis le 23/10 :
impossible d'identifier les meilleurs et pires posts de la semaine ni de savoir si les CTA binaires génèrent des commentaires.
- Action demandée à Annie : reconnecter le compte TikTok dans Metricool (Réglages > Connexions) et passer le compte en professionnel ; en attendant,
  relever à la main dans l'application TikTok les vues, commentaires et abonnés des 5 posts et du vote du 11/11.
- Leçon : sans données, on continue sur les formats qui marchaient en octobre (règles nommées, check-lists « X signes / X questions », idées reçues chiffrées).

## Lot du 9 novembre — planning 16-27/11 (forfait gratuit, 20 posts en novembre)
- Stock validé, remis en brouillon aux nouvelles dates (rotation après dormir-moins marine du 13/11) : 16 fermer-ta-journee (crème), 17 to-do-irrealiste (sauge),
  19 dose-en-3-mots (crème), 20 dire-non (sauge), 23 tout-est-important (marine), 26 dirigeant-gere-seul (marine).
- Nouveaux brouillons : 18/11 deleguer-sans-tout-perdre (marine, option 1 du vote), 24 dose-fait-le-poison (crème), 25 avant-une-reunion (sauge),
  27 syndrome-imposteur (crème). 1er/12 tete-qui-tourne-le-soir (marine, option 2 du vote, gardée pour décembre).
- SI L'OPTION 2 GAGNE LE VOTE : échanger les dates des deux posts (18/11 <-> 1er/12) et reprendre la phrase « Tu l'as choisi en commentaire » dans la légende du 18/11.
- Novembre = 20 publications avec ce planning : rien le 30/11.
