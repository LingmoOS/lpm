/*
 *  deps.h
 *
 *  Copyright (c) 2006-2024 Pacman Development Team <pacman-dev@lists.archlinux.org>
 *  Copyright (c) 2002-2006 by Judd Vinet <jvinet@zeroflux.org>
 *  Copyright (c) 2005 by Aurelien Foret <orelien@chez.com>
 *  Copyright (c) 2006 by Miklos Vajna <vmiklos@frugalware.org>
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
#ifndef ALPM_DEPS_H
#define ALPM_DEPS_H

#include "db.h"
#include "sync.h"
#include "package.h"
#include "alpm.h"

alpmepend_t *_alpmep_dup(const alpmepend_t *dep);
alpm_list_t *_alpm_sortbydeps(alpm_handle_t *handle,
		alpm_list_t *targets, alpm_list_t *ignore, int reverse);
int _alpm_recursedeps(alpmb_t *db, alpm_list_t **targs, int include_explicit);
int _alpm_resolvedeps(alpm_handle_t *handle, alpm_list_t *localpkgs, alpm_pkg_t *pkg,
		alpm_list_t *preferred, alpm_list_t **packages, alpm_list_t *remove,
		alpm_list_t **data);
int _alpmepcmp_literal(alpm_pkg_t *pkg, alpmepend_t *dep);
int _alpmepcmp_provides(alpmepend_t *dep, alpm_list_t *provisions);
int _alpmepcmp(alpm_pkg_t *pkg, alpmepend_t *dep);

#endif /* ALPM_DEPS_H */
