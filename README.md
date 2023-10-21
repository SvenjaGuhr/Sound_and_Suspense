# Sound and Suspense

This repository contains: 

## Annotation Guidelines:
- Guidelines for Ambient Sound Annotation
[https://github.com/SvenjaGuhr/Sound_and_Suspense/blob/main/Guidelines%20for%20Ambient%20Sound%20Annotation%20V1.1.pdf]

## Corpus and Subcorpora:
- Plain text corpus [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/Corpus_Sound_and_Suspense]
- Automatically suspense tagged subcorpus [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/suspense_auto_tagged_subcorpus]
- XML files with (semi-)manually sound annotated corpus texts usable as input training data for the software NEISS NTEE [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/annotated_data_for_NTEE]
- XML files without sound annotations usable as input prediction data for the software NEISS NTEE [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/xml_text_files_for_prediction]
- XML files with automatically sound annotated corpus texts [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/NTEE_sound_predicted_corpus] 

## Models:
Trained NEISS NTEE Models for automated sound annotation. The models can be regenerated using the indicated training data [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/annotated_data_for_NTEE]. For more information see the wiki of NEISS NTEE (TEI Entity Enricher) [https://github.com/NEISSproject/tei_entity_enricher].
- Model trained on Training Set 1 with six manually annotated texts
- Model trained on Training Set 2 with 11 manually and dictionary-annotated texts without correction of false positives
- Model trained on Training Set 3 with 13 manually and dictionary-annotated texts without correction of false positives
- Model trained on Training Set 4 with 13 manually and dictionary-annotated texts with correction of false positives
- Model trained on Training Set 5 with 15 manually and dictionary-annotated texts with correction of false positives

## Jupyter Notebooks:
- Preprocessing of plain text files as preparation for the manual sound annotation [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/Text_Preprocessing_for_Sound_Annotation]
- Converting XML-files to a dataframe [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/XML-files_to_dataframe]
- Sound annotation with dictionary approach [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/Sound_annotation_dictionary_approach]

## Dataframes:
- Dataframe with mapped manual annotations of sound and suspense for 4 texts with the generated plots in high resolution [https://github.com/SvenjaGuhr/Sound_and_Suspense/tree/main/Mapping_manual_sound_and_suspense_annotations]
- Corpus metadata table [https://github.com/SvenjaGuhr/Sound_and_Suspense/blob/main/Corpus_Metadata_update_09_2023.csv]

## Journal of Computational Literary Studies 
- Slides of Svenja Guhr's talk at the Conference of Computational Literary Studies (CCLS) on 23.06.2023 [https://github.com/SvenjaGuhr/Sound_and_Suspense/blob/main/Guhr_CCLS-talk_Sound_in_the_Gothic.pdf]
- Link to the Conference Version of the JCLS-Paper Guhr, Svenja & Algee-Hewitt, Mark. (2023). "What’s that Scary Sound? Ambient Sound in Gothic Fiction", in: Schöch, Christof, Gius, Evelyn, Trilcke, Peer, & Ripoll, Élodie. (2023). Conference Reader: 2nd Annual Conference of Computational Literary Studies (Version v1). 2nd Annual Conference of Computational Literary Studies (CCLS2023), Würzburg, Germany. Zenodo. [https://doi.org/10.5281/zenodo.8093598].

## License:
- Information on the GPL-3.0 license [https://github.com/SvenjaGuhr/Sound_and_Suspense/blob/main/LICENSE]
