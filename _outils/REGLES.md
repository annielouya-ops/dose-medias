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
