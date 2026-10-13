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
