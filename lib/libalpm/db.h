/*
 *  db.h
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
#ifndef ALPM_DB_H
#define ALPM_DB_H

/* libarchive */
#include <archive.h>
#include <archive_entry.h>

#include "alpm.h"
#include "pkghash.h"
#include "signing.h"

/* Database entries */
typedef enum _alpmbinfrq_t {
	INFRQ_BASE = (1 << 0),
	INFRQ_DESC = (1 << 1),
	INFRQ_FILES = (1 << 2),
	INFRQ_SCRIPTLET = (1 << 3),
	INFRQ_DSIZE = (1 << 4),
	/* ALL should be info stored in the package or database */
	INFRQ_ALL = INFRQ_BASE | INFRQ_DESC | INFRQ_FILES |
		INFRQ_SCRIPTLET | INFRQ_DSIZE,
	INFRQ_ERROR = (1 << 30)
} alpmbinfrq_t;

/** Database status. Bitflags. */
enum _alpmbstatus_t {
	DB_STATUS_VALID = (1 << 0),
	DB_STATUS_INVALID = (1 << 1),
	DB_STATUS_EXISTS = (1 << 2),
	DB_STATUS_MISSING = (1 << 3),

	DB_STATUS_LOCAL = (1 << 10),
	DB_STATUS_PKGCACHE = (1 << 11),
	DB_STATUS_GRPCACHE = (1 << 12)
};

struct db_operations {
	int (*validate) (alpmb_t *);
	int (*populate) (alpmb_t *);
	void (*unregister) (alpmb_t *);
};

/* Database */
struct _alpmb_t {
	alpm_handle_t *handle;
	char *treename;
	/* do not access directly, use _alpmb_path(db) for lazy access */
	char *_path;
	alpm_pkghash_t *pkgcache;
	alpm_list_t *grpcache;
	alpm_list_t *cache_servers;
	alpm_list_t *servers;
	const struct db_operations *ops;

	/* bitfields for validity, local, loaded caches, etc. */
	/* From _alpmbstatus_t */
	int status;
	/* alpm_siglevel_t */
	int siglevel;
	/* alpmb_usage_t */
	int usage;
};


/* db.c, database general calls */
alpmb_t *_alpmb_new(const char *treename, int is_local);
void _alpmb_free(alpmb_t *db);
const char *_alpmb_path(alpmb_t *db);
int _alpmb_cmp(const void *d1, const void *d2);
int _alpmb_search(alpmb_t *db, const alpm_list_t *needles,
		alpm_list_t **ret);
alpmb_t *_alpmb_register_local(alpm_handle_t *handle);
alpmb_t *_alpmb_register_sync(alpm_handle_t *handle, const char *treename,
		int level);
void _alpmb_unregister(alpmb_t *db);

/* be_*.c, backend specific calls */
int _alpm_local_db_prepare(alpmb_t *db, alpm_pkg_t *info);
int _alpm_local_db_write(alpmb_t *db, alpm_pkg_t *info, int inforeq);
int _alpm_local_db_remove(alpmb_t *db, alpm_pkg_t *info);
char *_alpm_local_db_pkgpath(alpmb_t *db, alpm_pkg_t *info, const char *filename);

/* cache bullshit */
/* packages */
void _alpmb_free_pkgcache(alpmb_t *db);
int _alpmb_add_pkgincache(alpmb_t *db, alpm_pkg_t *pkg);
int _alpmb_remove_pkgfromcache(alpmb_t *db, alpm_pkg_t *pkg);
alpm_pkghash_t *_alpmb_get_pkgcache_hash(alpmb_t *db);
alpm_list_t *_alpmb_get_pkgcache(alpmb_t *db);
alpm_pkg_t *_alpmb_get_pkgfromcache(alpmb_t *db, const char *target);
/* groups */
alpm_list_t *_alpmb_get_groupcache(alpmb_t *db);
alpm_group_t *_alpmb_get_groupfromcache(alpmb_t *db, const char *target);

#endif /* ALPM_DB_H */
