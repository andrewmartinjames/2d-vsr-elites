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
package it.units.erallab.hmsrobots.core.objects.immutable;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Eric Medvet <eric.medvet@gmail.com>
 */
public class Immutable {

  protected final List<Immutable> children;

  public Immutable() {
    this.children = new ArrayList<>();
  }

  public List<Immutable> getChildren() {
    return children;
  }
}