#!/usr/bin/env python3

import router

router1 = router.importrouter('i2_startup-config.cfg')
print(router1.tostring())
router.exception(router1)
