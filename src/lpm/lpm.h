/*
 *  lpm.h
 *
 *  Copyright (c) 2006-2024 Pacman Development Team <pacman-dev@lists.archlinux.org>
 *  Copyright (c) 2002-2006 by Judd Vinet <jvinet@zeroflux.org>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#ifndef PM_LPM_H
#define PM_LPM_H

#include <alpm_list.h>

#define LPM_CALLER_PREFIX "LPM"

/* database.c */
int lpmatabase(alpm_list_t *targets);
/* deptest.c */
int lpmeptest(alpm_list_t *targets);
/* files.c */
int lpm_files(alpm_list_t *files);
/* query.c */
int lpm_query(alpm_list_t *targets);
/* remove.c */
int lpm_remove(alpm_list_t *targets);
/* sync.c */
int lpm_sync(alpm_list_t *targets);
int sync_prepare_execute(void);
/* upgrade.c */
int lpm_upgrade(alpm_list_t *targets);

#endif /* PM_LPM_H */
