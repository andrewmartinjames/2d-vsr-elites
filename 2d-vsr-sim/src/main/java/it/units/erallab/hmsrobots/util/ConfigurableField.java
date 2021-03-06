/*
 * Copyright (C) 2020 Eric Medvet <eric.medvet@gmail.com> (as alikhan4812)
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful, but
 *  WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

package it.units.erallab.hmsrobots.util;

import javax.annotation.meta.TypeQualifier;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@TypeQualifier
@Retention(RetentionPolicy.RUNTIME)
public @interface ConfigurableField {

  enum Type {BASIC, ADVANCED}

  Type uiType() default Type.ADVANCED;

  Class<?> enumClass() default Void.class;

  double uiMin() default Double.NEGATIVE_INFINITY;

  double uiMax() default Double.POSITIVE_INFINITY;

}
