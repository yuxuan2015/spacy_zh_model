# coding: utf8
from __future__ import unicode_literals


VERBS_IRREG = {
     "είσαι": ("είμαι",),
     "είναι": ("είμαι",),
     "είμαστε": ("είμαι",),
     "είστε": ("είμαι",),
     "είσαστε": ("είμαι",),
     "ήμουν": ("είμαι",),
     "ήσουν": ("είμαι",),
     "ήταν": ("είμαι",),
     "ήμαστε": ("είμαι",),
     "ήμασταν": ("είμαι",),
     "ήταν": ("είμαι",),
     "είπα": ("λέω",),
     "είπες": ("λέω",),
     "είπε": ("λέω",),
     "είπαμε": ("λέω",),
     "είπατε": ("λέω",),
     "είπαν": ("λέω",),
     "είπανε": ("λέω",),
     "πει": ("λέω"),
     "πω": ("λέω"),
     "πάω": ("πηγαίνω",),
     "πάς": ("πηγαίνω",),
     "πας": ("πηγαίνω",),
     "πάει": ("πηγαίνω",),
     "πάμε": ("πηγαίνω",),
     "πάτε": ("πηγαίνω",),
     "πάνε": ("πηγαίνω",),
     "πήγα": ("πηγαίνω",),
     "πήγες": ("πηγαίνω",),
     "πήγε": ("πηγαίνω",),
     "πήγαμε": ("πηγαίνω",),
     "πήγατε": ("πηγαίνω",),
     "πήγαν": ("πηγαίνω",),
     "πήγανε": ("πηγαίνω",),
     "έπαιζα": ("παίζω",),
     "έπαιζες": ("παίζω",),
     "έπαιζε": ("παίζω",),
     "έπαιζαν": ("παίζω,",),
     "έπαιξα": ("παίζω",),
     "έπαιξες": ("παίζω",),
     "έπαιξε": ("παίζω",),
     "έτρωγα": ("τρώω",),
     "έτρωγες": ("τρώω",),
     "έτρωγε": ("τρώω",),
     "έτρωγαν": ("τρώω",),
     "είχα": ("έχω",),
     "είχες": ("έχω",),
     "είχε": ("έχω",),
     "είχαμε": ("έχω",),
     "είχατε": ("έχω",),
     "είχαν": ("έχω",),
     "είχανε": ("έχω",),
     "έπαιρνα": ("παίρνω",),
     "έπαιρνες": ("παίρνω",),
     "έπαιρνε": ("παίρνω",),
     "έπαιρναν": ("παίρνω",),
     "εδίνα": ("δίνω",),
     "εδίνες": ("δίνω",),
     "εδίνε": ("δίνω",),
     "εδίναν": ("δίνω",),
     "έκανα": ("κάνω",),
     "έκανες": ("κάνω",),
     "έκανε": ("κάνω",),
     "έκαναν": ("κάνω",),
     "ήθελα": ("θέλω",),
     "ήθελες": ("θέλω",),
     "ήθελε": ("θέλω",),
     "ήθελαν": ("θέλω",),
     "έβλεπα": ("βλέπω",),
     "έβλεπες": ("βλέπω",),
     "έβλεπε": ("βλέπω",),
     "έβλεπαν": ("βλέπω",),
     "είδα": ("βλέπω",),
     "είδες": ("βλέπω",),
     "είδε": ("βλέπω",),
     "είδαμε": ("βλέπω",),
     "είδατε": ("βλέπω",),
     "είδαν": ("βλέπω",),
     "έφερνα": ("φέρνω",),
     "έφερνες": ("φέρνω",),
     "έφερνε": ("φέρνω",),
     "έφερναν": ("φέρνω",),
     "έφερα": ("φέρω",),
     "έφερες": ("φέρω",),
     "έφερε": ("φέρω",),
     "έφεραν": ("φέρω",),
     "έλαβα": ("λαμβάνω",),
     "έλαβες": ("λαμβάνω",),
     "έλαβε": ("λαμβάνω",),
     "έλαβαν": ("λαμβάνω",),
     "έβρισκα": ("βρίσκω",),
     "έβρισκες": ("βρίσκω",),
     "έβρισκε": ("βρίσκω",),
     "έβρισκαν": ("βρίσκω",),
     "ήξερα": ("ξέρω",),
     "ήξερες": ("ξέρω",),
     "ήξερε": ("ξέρω",),
     "ήξεραν": ("ξέρω",),
     "ανέφερα": ("αναφέρω",),
     "ανέφερες": ("αναφέρω",),
     "ανέφερε": ("αναφέρω",),
     "ανέφεραν": ("αναφέρω",),
     "έβαζα": ("βάζω",),
     "έβαζες": ("βάζω",),
     "έβαζε": ("βάζω",),
     "έβαζαν": ("βάζω",),
     "έμεινα": ("μένω",),
     "έμεινες": ("μένω",),
     "έμεινε": ("μένω",),
     "έμειναν": ("μένω",),
     "έβγαζα": ("βγάζω",),
     "έβγαζες": ("βγάζω",),
     "έβγαζε": ("βγάζω",),
     "έβγαζαν": ("βγάζω",),
     "έμπαινα": ("μπαίνω",),
     "έμπαινες": ("μπαίνω",),
     "έμπαινε": ("μπαίνω",),
     "έμπαιναν": ("μπαίνω",),
     "βγήκα": ("βγαίνω",),
     "βγήκες": ("βγαίνω",),
     "βγήκε": ("βγαίνω",),
     "βγήκαμε": ("βγαίνω",),
     "βγήκατε": ("βγαίνω",),
     "βγήκαν": ("βγαίνω",),
     "έπεφτα": ("πέφτω",),
     "έπεφτες": ("πέφτω",),
     "έπεφτε": ("πέφτω",),
     "έπεφταν": ("πέφτω",),
     "έπεσα": ("πέφτω",),
     "έπεσες": ("πέφτω",),
     "έπεσε": ("πέφτω",),
     "έπεσαν": ("πέφτω",),
     "έστειλα": ("στέλνω",),
     "έστειλες": ("στέλνω",),
     "έστειλε": ("στέλνω",),
     "έστειλαν": ("στέλνω",),
     "έφυγα": ("φεύγω",),
     "έφυγες": ("φεύγω",),
     "έφυγες": ("φεύγω",),
     "έφυγαν": ("φεύγω",),
     "έμαθα": ("μαθαίνω",),
     "έμαθες": ("μαθαίνω",),
     "έμαθε": ("μαθαίνω",),
     "έμαθαν": ("μαθαίνω",),
     "υπέβαλλα": ("υποβάλλω",),
     "υπέβαλλες": ("υποβάλλω",),
     "υπέβαλλε": ("υποβάλλω",),
     "υπέβαλλαν": ("υποβάλλω",),
     "έπινα": ("πίνω",),
     "έπινες": ("πίνω",),
     "έπινε": ("πίνω",),
     "έπιναν": ("πίνω",),
     "ήπια": ("πίνω",),
     "ήπιες": ("πίνω",),
     "ήπιε": ("πίνω",),
     "ήπιαμε": ("πίνω",),
     "ήπιατε": ("πίνω",),
     "ήπιαν": ("πίνω",),
     "ετύχα": ("τυχαίνω",),
     "ετύχες": ("τυχαίνω",),
     "ετύχε": ("τυχαίνω",),
     "ετύχαν": ("τυχαίνω",),
     "φάω": ("τρώω",),
     "φάς": ("τρώω",),
     "φάει": ("τρώω",),
     "φάμε": ("τρώω",),
     "φάτε": ("τρώω",),
     "φάνε": ("τρώω",),
     "φάν": ("τρώω",),
     "έτρωγα": ("τρώω",),
     "έτρωγες": ("τρώω",),
     "τρώγαμε": ("τρώω",),
     "τρώγατε": ("τρώω",),
     "τρώγανε": ("τρώω",),
     "τρώγαν": ("τρώω",),
     "πέρασα": ("περνώ",),
     "πέρασες": ("περνώ",),
     "πέρασε": ("περνώ",),
     "πέρασαμε": ("περνώ",),
     "πέρασατε": ("περνώ",),
     "πέρασαν": ("περνώ",),
     "έγδαρα": ("γδάρω",),
     "έγδαρες": ("γδάρω",),
     "έγδαρε": ("γδάρω",),
     "έγδαραν": ("γδάρω",),
     "έβγαλα": ("βγάλω",),
     "έβγαλες": ("βγάλω",),
     "έβγαλε": ("βγάλω",),
     "έβγαλαν": ("βγάλω",),
     "έφθασα": ("φτάνω",),
     "έφθασες": ("φτάνω",),
     "έφθασε": ("φτάνω",),
     "έφθασαν": ("φτάνω",),

}
